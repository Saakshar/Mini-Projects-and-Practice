from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/dataset/weights/best.pt")
results = model("test_image.jpg")

for r in results:
    print(r.boxes)  # bounding boxes, confidences, etc.
    r.show()        # opens an annotated image window
