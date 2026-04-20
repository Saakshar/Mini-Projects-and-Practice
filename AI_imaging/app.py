from flask import Flask, request, render_template_string, send_from_directory
from ultralytics import YOLO
import cv2, os, uuid

app = Flask(__name__)
model = YOLO('runs/detect/train/weights/best.pt')

# Make sure we have a folder for output
UPLOAD_FOLDER = os.path.join(app.root_path, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML = """
<!doctype html>
<title>Green Crab Detector</title>
<h2>Upload image</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
{% if img %}
  <h3>Result</h3>
  <img src="{{ img }}" style="max-width:800px">
{% endif %}
"""

@app.route('/', methods=['GET','POST'])
def index():
    img_url = None
    if request.method == 'POST':
        f = request.files['file']
        fname = f"{uuid.uuid4().hex}.jpg"
        fpath = os.path.join(UPLOAD_FOLDER, fname)
        f.save(fpath)

        results = model.predict(source=fpath, conf=0.25, imgsz=640)
        r = results[0]

        img = cv2.imread(fpath)
        for box in r.boxes:
            x1,y1,x2,y2 = map(int, box.xyxy[0].tolist())
            conf = float(box.conf[0])
            cv2.rectangle(img, (x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(img, f'{conf:.2f}', (x1,y1-6),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

        out_name = f"out_{uuid.uuid4().hex}.jpg"
        out_path = os.path.join(UPLOAD_FOLDER, out_name)
        cv2.imwrite(out_path, img)

        # URL for <img src="...">
        img_url = f"/static/uploads/{out_name}"

    return render_template_string(HTML, img=img_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000,use_reloader=False)
