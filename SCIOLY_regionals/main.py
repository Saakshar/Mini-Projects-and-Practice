"""
Science Olympiad Florida — Event Chart Generator GUI
=====================================================
Run with:  python scioly_event_chart_gui.py

Requires scioly_event_chart.py to be in the same directory.
"""

import io
import math
import re
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

import requests
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from bs4 import BeautifulSoup

# ── Inline copy of the core logic (no import dependency) ──────────────────

BASE_URL         = "https://scilympiad.com/fl"
TOUR_RESULTS_URL = f"{BASE_URL}/Info/TourResults"
TARGET_TEAMS     = 42

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

DIST_COLORS = [
    "#E05C5C", "#E09B3D", "#4C9BE8",
    "#6FCF97", "#BB6BD9", "#F06292",
]


def get_division_c_tournaments(session):
    resp = session.get(TOUR_RESULTS_URL, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    tournaments = []
    for tag in soup.find_all("h4"):
        text = tag.get_text(strip=True)
        if "Division C" not in text:
            continue
        link = tag.find("a")
        if not link:
            continue
        href = link.get("href", "")
        if not href.startswith("http"):
            href = BASE_URL + href
        parts    = text.split(" - ")
        district = parts[1].strip() if len(parts) > 1 else text
        if " at " in district:
            district = district.split(" at ")[0].strip()
        tournaments.append({"district": district, "url": href})
    return tournaments


def scrape_event(session, tournament, event_name, log):
    resp = session.get(tournament["url"], headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup  = BeautifulSoup(resp.text, "html.parser")
    table = soup.find("table")
    if not table:
        return [], 0, 0

    hrow          = table.find("tr")
    headers       = [th.get_text(strip=True) for th in hrow.find_all(["th", "td"])]
    headers_lower = [h.lower() for h in headers]
    event_lower   = event_name.lower()

    if event_lower in headers_lower:
        ev_idx = headers_lower.index(event_lower)
    else:
        matches = [i for i, h in enumerate(headers_lower) if event_lower in h]
        if not matches:
            log(f"  ✗  '{event_name}' not found in {tournament['district']}")
            log(f"     Available: {', '.join(headers[3:])}")
            return [], 0, 0
        ev_idx = matches[0]
        log(f"  ~  Matched '{event_name}' → '{headers[ev_idx]}' ({tournament['district']})")

    try:
        team_idx  = headers_lower.index("school/team")
        place_idx = headers_lower.index("place")
    except ValueError:
        return [], 0, 0

    total_reg = 0
    for row in table.find_all("tr"):
        m = re.search(r"Total Teams:\s*(\d+)", row.get_text())
        if m:
            total_reg = int(m.group(1))
            break

    all_rows = []
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) <= ev_idx:
            continue
        try:
            ev_val    = int(cols[ev_idx].get_text(strip=True))
            team_name = cols[team_idx].get_text(strip=True)
            ovr_raw   = cols[place_idx].get_text(strip=True)
            overall   = int(re.match(r"(\d+)", ovr_raw).group(1))
            all_rows.append({"team": team_name, "overall": overall, "event": ev_val})
        except (ValueError, AttributeError, IndexError):
            continue

    if not all_rows or total_reg == 0:
        return [], total_reg, 0

    penalty  = total_reg + 1
    competed = [r for r in all_rows if r["event"] != penalty]
    if not competed:
        competed = all_rows
    return competed, total_reg, penalty


def compute_quotas(district_totals, target):
    grand  = sum(district_totals.values())
    raw    = {d: target * t / grand for d, t in district_totals.items()}
    floors = {d: int(q) for d, q in raw.items()}
    remain = target - sum(floors.values())
    fracs  = sorted(raw.keys(), key=lambda d: -(raw[d] - floors[d]))
    quotas = dict(floors)
    for d in fracs[:remain]:
        quotas[d] += 1
    return quotas


def score(placement, competitors):
    return (100 / competitors) * (competitors - placement)


def nickname(name, maxlen=46):
    if "," in name:
        nick = name.split(",", 1)[1].strip()
        return (nick[:maxlen - 1] + "…") if len(nick) > maxlen else nick
    return (name[:maxlen - 1] + "…") if len(name) > maxlen else name


def build_chart(all_entries, district_meta, event_name, color_map):
    n     = len(all_entries)
    scores    = [e["score"] for e in all_entries]
    max_score = max(scores)
    y_pos     = list(range(n - 1, -1, -1))

    fig, ax = plt.subplots(figsize=(17, max(14, n * 0.52 + 4)))
    fig.patch.set_facecolor("#0D0F18")
    ax.set_facecolor("#181B28")
    for sp in ax.spines.values():
        sp.set_edgecolor("#2E3150")

    bars = ax.barh(
        y_pos, scores,
        color=[color_map[e["district"]] for e in all_entries],
        height=0.72, edgecolor="#0D0F18", linewidth=0.8,
    )

    for j, (bar, entry) in enumerate(zip(bars, all_entries)):
        sc    = entry["score"]
        by    = bar.get_y() + bar.get_height() / 2
        nick  = nickname(entry["team"])
        color = color_map[entry["district"]]

        if sc > max_score * 0.35:
            ax.text(sc * 0.97, by, nick,
                    va="center", ha="right", color="#0D0F18",
                    fontsize=8.2, fontweight="bold",
                    path_effects=[pe.withStroke(linewidth=1, foreground="#0D0F18")])
        else:
            ax.text(sc + max_score * 0.008, by, nick,
                    va="center", ha="left", color=color,
                    fontsize=8.2, fontweight="bold")

        ax.text(max_score * 1.005, by,
                f"  {sc:.1f}%  "
                f"(#{entry['event_place']} / {entry['competitors']}  |  "
                f"ovr #{entry['overall']})",
                va="center", ha="left", color=color, fontsize=7.8)

    for idx in range(0, n, 2):
        ax.axhspan(y_pos[idx] - 0.42, y_pos[idx] + 0.42,
                   color="#1E2130", zorder=0, linewidth=0)

    ax.axvline(50, color="#666688", linewidth=1.0, linestyle="--", zorder=4)
    ax.text(50.5, n - 0.15, "50% — beat half the field",
            color="#666688", fontsize=7.5, va="top", ha="left")

    if n >= 10:
        ax.axhline(y_pos[9] - 0.5, color="#FFD700",
                   linewidth=0.8, linestyle="--", zorder=3, alpha=0.5)
        ax.text(max_score * 1.62, y_pos[9] - 0.3, "── Top 10",
                color="#FFD700", fontsize=7.5, va="top", ha="right", alpha=0.7)

    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"],
                       color="#555577", fontsize=8)
    ax.tick_params(axis="x", length=3, color="#2E3150")
    ax.set_yticks(y_pos)
    ax.set_yticklabels([f"#{r + 1}" for r in range(n)],
                       color="#AAAACC", fontsize=8.5)
    ax.tick_params(axis="y", length=0, pad=5)
    ax.set_xlim(0, max_score * 1.72)
    ax.set_ylim(-0.65, n - 0.35)
    ax.xaxis.grid(True, color="#22253A", linewidth=0.5, linestyle="--")
    ax.set_axisbelow(True)

    legend_patches = [
        mpatches.Patch(
            color=color_map[d],
            label=(f"{d}  "
                   f"({district_meta[d]['quota']}/{district_meta[d]['total_reg']} teams  |  "
                   f"{district_meta[d]['competitors']} competitors)")
        )
        for d in district_meta
    ]
    ax.legend(handles=legend_patches, loc="lower right",
              framealpha=0.22, facecolor="#0D0F18", edgecolor="#2E3150",
              labelcolor="white", fontsize=8.5,
              title="District  (quota / registered  |  event field size)",
              title_fontsize=8.5, labelspacing=0.65)

    ax.text(0.002, -0.025,
            "Score = (100 ÷ competitors) × (competitors − placement)   ·   "
            "% of district event field beaten   ·   "
            f"{TARGET_TEAMS} teams selected proportionally by district size",
            transform=ax.transAxes, color="#555577", fontsize=8, ha="left")

    ax.set_title(
        f"Science Olympiad Florida 2026  ·  Division C  ·  {event_name}\n"
        f"{n} Teams — Proportional District Representation — % of Field Beaten",
        color="white", fontsize=13, fontweight="bold", pad=14, loc="left",
    )

    plt.tight_layout(pad=2.0)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=130,
                bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.savefig(f"{event_name.replace(' ', '_')}_results.png", dpi=150,
                bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return buf


# ── GUI ────────────────────────────────────────────────────────────────────

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Science Olympiad — Event Chart Generator")
        self.configure(bg="#0D0F18")
        self.resizable(True, True)
        self.minsize(700, 500)

        self._build_ui()
        self._chart_image = None   # keep PIL reference alive

    def _build_ui(self):
        # ── Header ──────────────────────────────────────────────────────────
        hdr = tk.Frame(self, bg="#181B28", pady=14)
        hdr.pack(fill="x")
        tk.Label(
            hdr,
            text="Science Olympiad Florida 2026  ·  Division C",
            font=("Helvetica", 13, "bold"),
            bg="#181B28", fg="#CCCCEE",
        ).pack()
        tk.Label(
            hdr,
            text="Event Chart Generator",
            font=("Helvetica", 11),
            bg="#181B28", fg="#555577",
        ).pack()

        # ── Input row ───────────────────────────────────────────────────────
        input_frame = tk.Frame(self, bg="#0D0F18", pady=14, padx=20)
        input_frame.pack(fill="x")

        tk.Label(
            input_frame, text="Event name:",
            font=("Helvetica", 11), bg="#0D0F18", fg="#AAAACC",
        ).pack(side="left", padx=(0, 10))

        self.event_var = tk.StringVar(value="Robot Tour")
        self.entry = tk.Entry(
            input_frame,
            textvariable=self.event_var,
            font=("Helvetica", 12),
            bg="#181B28", fg="white",
            insertbackground="white",
            relief="flat",
            bd=0,
            width=28,
        )
        self.entry.pack(side="left", ipady=6, padx=(0, 12))
        self.entry.bind("<Return>", lambda _: self._start_generate())

        self.gen_btn = tk.Button(
            input_frame,
            text="Generate Chart",
            font=("Helvetica", 11, "bold"),
            bg="#4C9BE8", fg="white",
            activebackground="#3a7bc8",
            activeforeground="white",
            relief="flat", bd=0,
            padx=18, pady=6,
            cursor="hand2",
            command=self._start_generate,
        )
        self.gen_btn.pack(side="left")

        self.save_btn = tk.Button(
            input_frame,
            text="💾  Save PNG",
            font=("Helvetica", 10),
            bg="#2E3150", fg="#AAAACC",
            activebackground="#3a3f66",
            activeforeground="white",
            relief="flat", bd=0,
            padx=14, pady=6,
            cursor="hand2",
            command=self._save_image,
            state="disabled",
        )
        self.save_btn.pack(side="left", padx=(8, 0))

        # ── Progress / log ───────────────────────────────────────────────────
        log_frame = tk.Frame(self, bg="#0D0F18", padx=20)
        log_frame.pack(fill="x")

        self.progress = ttk.Progressbar(
            log_frame, mode="indeterminate", length=400
        )
        self.progress.pack(side="left", pady=(0, 6))

        self.status_var = tk.StringVar(value="Enter an event name and click Generate.")
        tk.Label(
            log_frame,
            textvariable=self.status_var,
            font=("Helvetica", 9),
            bg="#0D0F18", fg="#666688",
            anchor="w",
        ).pack(side="left", padx=12)

        # Scrollable log box
        log_box_frame = tk.Frame(self, bg="#0D0F18", padx=20)
        log_box_frame.pack(fill="x")
        self.log_box = tk.Text(
            log_box_frame,
            height=5, font=("Courier", 9),
            bg="#181B28", fg="#666688",
            relief="flat", state="disabled",
            wrap="word",
        )
        self.log_box.pack(fill="x")

        # ── Chart canvas (scrollable) ────────────────────────────────────────
        canvas_outer = tk.Frame(self, bg="#0D0F18", padx=20, pady=10)
        canvas_outer.pack(fill="both", expand=True)

        self.canvas_frame = tk.Frame(canvas_outer, bg="#0D0F18")
        self.canvas_frame.pack(fill="both", expand=True)

        self.v_scroll = tk.Scrollbar(self.canvas_frame, orient="vertical",
                                     bg="#181B28", troughcolor="#0D0F18")
        self.v_scroll.pack(side="right", fill="y")

        self.h_scroll = tk.Scrollbar(self.canvas_frame, orient="horizontal",
                                     bg="#181B28", troughcolor="#0D0F18")
        self.h_scroll.pack(side="bottom", fill="x")

        self.canvas = tk.Canvas(
            self.canvas_frame,
            bg="#0D0F18", highlightthickness=0,
            yscrollcommand=self.v_scroll.set,
            xscrollcommand=self.h_scroll.set,
        )
        self.canvas.pack(fill="both", expand=True)
        self.v_scroll.config(command=self.canvas.yview)
        self.h_scroll.config(command=self.canvas.xview)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)

        self._img_item = None

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _log(self, msg):
        """Append a line to the log box (thread-safe via after)."""
        def _append():
            self.log_box.config(state="normal")
            self.log_box.insert("end", msg + "\n")
            self.log_box.see("end")
            self.log_box.config(state="disabled")
        self.after(0, _append)

    def _set_status(self, msg):
        self.after(0, lambda: self.status_var.set(msg))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _save_image(self):
        if not hasattr(self, "_last_buf") or self._last_buf is None:
            return
        from tkinter.filedialog import asksaveasfilename
        path = asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG image", "*.png")],
            initialfile=f"{self.event_var.get().replace(' ', '_')}_results.png",
        )
        if path:
            self._last_buf.seek(0)
            with open(path, "wb") as f:
                f.write(self._last_buf.read())
            messagebox.showinfo("Saved", f"Chart saved to:\n{path}")

    # ── Generation pipeline ───────────────────────────────────────────────

    def _start_generate(self):
        event = self.event_var.get().strip()
        if not event:
            messagebox.showwarning("No event", "Please enter an event name.")
            return

        # Clear log and previous chart
        self.log_box.config(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.config(state="disabled")
        if self._img_item:
            self.canvas.delete(self._img_item)
        self._chart_image = None
        self.save_btn.config(state="disabled")

        self.gen_btn.config(state="disabled", text="Generating…")
        self.progress.start(12)
        self._set_status(f"Fetching data for '{event}' …")

        thread = threading.Thread(target=self._generate, args=(event,), daemon=True)
        thread.start()

    def _generate(self, event_name):
        try:
            with requests.Session() as session:
                self._log("Fetching tournament list …")
                tournaments = get_division_c_tournaments(session)
                self._log(f"Found {len(tournaments)} Division C tournament(s).")

                district_data = {}
                for t in tournaments:
                    self._log(f"Scraping: {t['district']} …")
                    self._set_status(f"Scraping {t['district']} …")
                    competed, total_reg, penalty = scrape_event(
                        session, t, event_name, self._log
                    )
                    if not competed:
                        self._log(f"  → No data, skipping.")
                        continue
                    self._log(f"  → {len(competed)} competitors (penalty={penalty})")
                    district_data[t["district"]] = {
                        "total_reg":   total_reg,
                        "competitors": len(competed),
                        "teams":       sorted(competed, key=lambda x: x["overall"]),
                    }

                if not district_data:
                    self.after(0, lambda: messagebox.showerror(
                        "Event not found",
                        f"No districts had data for '{event_name}'.\n"
                        "Check spelling — it must match the column header on the site."
                    ))
                    return

                totals = {d: v["total_reg"] for d, v in district_data.items()}
                quotas = compute_quotas(totals, TARGET_TEAMS)
                for d, q in quotas.items():
                    district_data[d]["quota"] = q
                    self._log(f"  Quota {d}: {q}/{totals[d]}")

                color_map = {
                    d: DIST_COLORS[i % len(DIST_COLORS)]
                    for i, d in enumerate(district_data.keys())
                }

                all_entries = []
                for district, data in district_data.items():
                    p     = data["competitors"]
                    quota = data["quota"]
                    for row in data["teams"][:quota]:
                        all_entries.append({
                            "team":        row["team"],
                            "district":    district,
                            "overall":     row["overall"],
                            "event_place": row["event"],
                            "competitors": p,
                            "total_reg":   data["total_reg"],
                            "score":       score(row["event"], p),
                        })

                all_entries.sort(key=lambda x: (-x["score"], x["event_place"]))

                self._set_status("Rendering chart …")
                self._log("Building chart …")

                district_meta = {
                    d: {"total_reg":   district_data[d]["total_reg"],
                        "competitors": district_data[d]["competitors"],
                        "quota":       district_data[d]["quota"]}
                    for d in district_data
                }

                buf = build_chart(all_entries, district_meta, event_name, color_map)
                self._last_buf = buf

                # Render in GUI on main thread
                self.after(0, lambda: self._display_chart(buf, event_name))

        except requests.exceptions.ConnectionError:
            self.after(0, lambda: messagebox.showerror(
                "Connection Error",
                "Could not reach scilympiad.com.\nCheck your internet connection."
            ))
        except Exception as exc:
            import traceback
            self._log(f"ERROR: {exc}")
            self._log(traceback.format_exc())
            self.after(0, lambda: messagebox.showerror("Error", str(exc)))
        finally:
            self.after(0, self._reset_ui)

    def _display_chart(self, buf, event_name):
        buf.seek(0)
        pil_img = Image.open(buf)
        self._chart_image = ImageTk.PhotoImage(pil_img)

        w, h = pil_img.size
        self.canvas.config(scrollregion=(0, 0, w, h))

        if self._img_item:
            self.canvas.delete(self._img_item)
        self._img_item = self.canvas.create_image(0, 0, anchor="nw",
                                                  image=self._chart_image)
        self._set_status(f"✅  Done — {event_name}_results.png also saved to disk.")
        self.save_btn.config(state="normal")

    def _reset_ui(self):
        self.progress.stop()
        self.gen_btn.config(state="normal", text="Generate Chart")


# ── Entry point ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        from PIL import Image, ImageTk
    except ImportError:
        import subprocess, sys
        subprocess.check_call([sys.executable, "-m", "pip", "install",
                               "Pillow", "--break-system-packages", "-q"])
        from PIL import Image, ImageTk

    app = App()
    app.geometry("1100x820")
    app.mainloop()