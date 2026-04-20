import cv2
import csv
from pathlib import Path
from ultralytics import YOLO

# Load trained YOLOv8 model
model = YOLO("runs/detect/train/weights/best.pt")

def detect_image(image_path, output_folder="output_detected", conf=0.25):
    """
    Detect objects in a single image, draw bounding boxes,
    and return a list of detections.
    Always returns at least one row for the image.
    """
    detections = []

    # Run YOLO prediction
    results = model.predict(source=str(image_path), conf=conf, imgsz=640)

    # Load original image
    img = cv2.imread(str(image_path))

    # Draw bounding boxes if any
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].int().tolist()
            conf_score = float(box.conf[0])

            # Draw rectangle
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Put label
            label = f"Green Crab {conf_score:.2f}"
            cv2.putText(img, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Append detection
            detections.append([image_path.name, "Green Crab", x1, y1, x2, y2, conf_score])

    # If no detections, add a row with zeros
    if not detections:
        detections.append([image_path.name, "None", 0, 0, 0, 0, 0])

    # Ensure output folder exists
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    output_path = Path(output_folder) / image_path.name

    # Save image
    cv2.imwrite(str(output_path), img)
    print(f"✅ Processed {image_path.name} → {output_path}")

    return detections

if __name__ == "__main__":
    # Hardcoded folder path for IDE usage
    folder_path = Path("test_images")  # <-- change this to your image folder
    output_folder = "output_detected"
    csv_file = "detections.csv"

    if not folder_path.is_dir():
        print("Error: Provided path is not a folder")
        exit()

    # Open CSV once and flush after each image
    with open(csv_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "class", "x1", "y1", "x2", "y2", "confidence"])

        # Process all images
        for image_file in folder_path.glob("*.*"):
            if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                dets = detect_image(image_file, output_folder=output_folder)
                writer.writerows(dets)
                f.flush()  # Ensure CSV is updated immediately

    print(f"\n✅ All detections (including negatives) saved to {csv_file}")
