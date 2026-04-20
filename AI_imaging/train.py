from ultralytics import YOLO
import os

# Load pretrained YOLOv8n
model = YOLO("yolov8n.pt")
unrefined_directory=os.listdir('runs/detect/')
print(unrefined_directory)

# Train on your dataset
model.train(data="data.yaml", epochs=50, imgsz=640)
# ***increase number of epochs to improve accuracy of detection***

# Manage and remove unnecessary training data
unrefined_directory=os.listdir('runs/detect/')
trained_directory=[folder for folder in unrefined_directory if 'train' in folder]
for folder in trained_directory:
    train_file_path=f'runs/detect/{folder}/'
    if not os.listdir(train_file_path):
        os.rmdir(train_file_path)