from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Or yolov8s.pt for better accuracy

# Set up input/output paths
input_dir = "../data"
output_dir = "../outputs"
os.makedirs(output_dir, exist_ok=True)

# Loop through all .mp4 files in the data directory
for filename in os.listdir(input_dir):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"processed_{filename}")

        # Open video file
        cap = cv2.VideoCapture(input_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Prepare output video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        print(f"🔄 Processing {filename}...")
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            annotated_frame = results[0].plot()
            out.write(annotated_frame)

        cap.release()
        out.release()
        print(f"✅ Done! Saved to {output_path}")

print("🎉 All videos processed!")
