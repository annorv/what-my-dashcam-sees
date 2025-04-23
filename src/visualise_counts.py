import json
import matplotlib.pyplot as plt
import os

# Load object counts
with open("../outputs/object_counts.json") as f:
    data = json.load(f)

# Create a bar chart per video
for video, counts in data.items():
    objects = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(8, 5))
    plt.bar(objects, values, color="skyblue")
    plt.title(f"Detected Objects in {video}")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    filename = f"../outputs/{video}_bar_chart.png"
    plt.savefig(filename)
    plt.close()
    print(f"📊 Saved chart: {filename}")
