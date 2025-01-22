from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO('yolov8n.pt')
print("Heloo world")
# Perform inference on an image
results = model('image.jpg')

# Display the results
results.show()

