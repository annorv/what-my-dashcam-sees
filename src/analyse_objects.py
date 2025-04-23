from ultralytics import YOLO
import cv2
import os
from collections import Counter
import json

# Paths
input_dir = "../data"
summary_path = "../outputs/object_counts.json"

# Load model
model = YOLO("yolov8n.pt")

summary = {}

# Analyse each video
for filename in os.listdir(input_dir):
    if filename.endswith(".mp4"):
        video_path = os.path.join(input_dir, filename)
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        object_counter = Counter()

        print(f"🔍 Analyzing {filename}...")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % 10 == 0:  # Analyze every 10th frame for speed
                results = model(frame)
                classes = results[0].boxes.cls.tolist()
                names = [model.names[int(cls)] for cls in classes]
                object_counter.update(names)
            frame_count += 1

        cap.release()
        summary[filename] = dict(object_counter)
        print(f"✅ Done: {filename}")

# Save results to JSON
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2)

print("📊 Object counts saved to object_counts.json")
