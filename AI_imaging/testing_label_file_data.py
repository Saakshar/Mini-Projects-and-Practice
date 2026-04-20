from pathlib import Path

labels_folder = Path("datasets/greencrab/train/labels")
for txt_file in labels_folder.glob("*.txt"):
    if not txt_file.read_text().strip():
        print(f"{txt_file.name} has no crabs (empty labels) ✅")