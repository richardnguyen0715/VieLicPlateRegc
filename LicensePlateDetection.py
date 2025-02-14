from ultralytics import YOLO

# Load a COCO-pretrained YOLOv11n model
model = YOLO("yolov11n.pt")

# Display model information
model.info()

# Train the model on the dataset for 80 epochs
results = model.train(data="data.yaml", epochs=80, imgsz=640)

# Test the model with for image here!
# path = ...
# testResult = model(path)