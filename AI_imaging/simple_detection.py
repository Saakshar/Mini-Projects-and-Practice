from ultralytics import YOLO

# Load your trained model (replace with your own path if different)
model = YOLO("runs/detect/train/weights/best.pt")

# Run prediction on a single image
results = model("test_images/example.jpg", save=True, show=True)

# Run prediction on a folder of images
# results = model("test_images/", save=True)

# Access predictions programmatically
for r in results:
    boxes = r.boxes.xyxy  # bounding boxes (x1, y1, x2, y2)
    confs = r.boxes.conf  # confidence scores
    cls = r.boxes.cls     # class IDs
    print("Boxes:", boxes)
    print("Confs:", confs)
    print("Classes:", cls)
