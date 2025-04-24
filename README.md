# What My Dash Cam Sees

**What My Dash Cam Sees** is an AI-powered Streamlit app that processes dash cam footage to detect and visualize common road objects in real-time — including cars, pedestrians, traffic signs, and more.

Built as a computer vision portfolio project by [Veronica](https://www.linkedin.com/in/veronica-a-7a905810b/), this tool combines cutting-edge object detection (YOLOv8) with intuitive visual insights for safer, smarter roads.

---

## 🚗 Features

- 🎞️ Upload and process dash cam video clips (MP4)
- 🔍 Detect objects like vehicles, people, traffic lights, and stop signs
- 🔁 Optional object tracking using Deep SORT
- 📊 Visualise object counts and trends with interactive charts
- 💾 Download processed videos and insights
- 🎛️ Sidebar filters by video and object type
- 🧠 Built with Python, Streamlit, YOLOv8, and Plotly

---

## 🛠️ Tech Stack

- `Python 3.10+`
- `YOLOv8 (Ultralytics)`
- `OpenCV`
- `Streamlit`
- `Plotly`
- `Matplotlib`
- `FFmpeg`

---

## 🔧 Setup Notes

Note: Due to file size limits on GitHub, the data/ and outputs/ folders are not included in this repo.
To run this project:
Create a data/ folder and place your dash cam .mp4 or .mov files inside it.
Create an empty outputs/ folder — this is where processed videos will be saved.

---


## 📂 Folder Structure

what-my-dashcam-sees/ ├── app/ │ ├── app.py │ └── utils.py ├── src/ │ └── process_videos.py ├── data/ │ └── input/ ← Your MP4 clips ├── outputs/ │ └── processed/ ← AI-tagged videos + data ├── requirements.txt └── README.md


---

## 🚀 Run It Locally

```bash
git clone https://github.com/annorv/what-my-dashcam-sees.git
cd what-my-dashcam-sees
pip install -r requirements.txt
streamlit run app/app.py
```

Why I Built This

I wanted to turn everyday dash cam footage into an interactive AI project, blending computer vision with storytelling and public safety. This app is part of my journey learning, building, and sharing with others in tech.

⭐ Support This Project

If you found this project inspiring or helpful:

- ⭐ Star this repo
- 👩🏽‍💻 Connect with me on LinkedIn
- 🔁 Share it with others learning AI and computer vision!

---