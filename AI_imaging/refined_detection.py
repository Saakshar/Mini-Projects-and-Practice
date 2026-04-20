from ultralytics import YOLO
import cv2

model = YOLO('runs/detect/train/weights/best.pt')  # or path to trained best.pt

def detect_image(img_path, conf=0.25):
    results = model.predict(source=img_path, conf=conf, imgsz=640)
    # results is a list; take first item
    r = results[0]
    img = cv2.imread(img_path)
    for box in r.boxes:
        x1,y1,x2,y2 = map(int, box.xyxy[0].tolist())
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(img, f'green_crab {conf:.2f}', (x1, y1-6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.imwrite('out.jpg', img)
    return 'out.jpg'

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        img_path = sys.argv[1]
    else:
        img_path = "test_images/example.jpg"  # default image

    out=detect_image(img_path)
    print('Saved', out)
