import streamlit as st
import os
import json

st.set_page_config(page_title="What My Dash Cam Sees", layout="wide")
st.title("🚘 What My Dash Cam Sees")
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
    }
    .video-wrapper {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 2rem;
        background-color: #f9f9f9;
    }
    .section-title {
        font-size: 1.5rem;
        margin-top: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True
)

# 📘 Section: Project Summary
st.markdown('<div class="section-title"> Project Summary</div>', unsafe_allow_html=True)
st.info("""
This app analyses dash cam footage to detect and track objects like cars, pedestrians, and traffic lights.

It uses:
- **YOLOv8** for real-time object detection
- **OpenCV** and **Matplotlib** for frame-by-frame analysis
- **Streamlit** for interactivity and sharing

Built by **Veronica** as part of *Veronica’s Data Path* .
""")


# 🎥 Section: Processed Videos
st.markdown('<div class="section-title">🎥 Processed Dash Cam Clips</div>', unsafe_allow_html=True)
video_files = sorted([f for f in os.listdir("../outputs") if f.endswith(".mp4")])

if video_files:
    for filename in video_files:
        with st.expander(f"▶ {filename}", expanded=False):
            st.video(f"../outputs/{filename}")
else:
    st.warning("No processed videos found.")

# 📊 Section: Object Counts & Visuals
counts_path = "../outputs/object_counts.json"
if os.path.exists(counts_path):
    st.markdown('<div class="section-title">📊 Object Counts Per Video</div>', unsafe_allow_html=True)
    with open(counts_path) as f:
        object_counts = json.load(f)

    for video_name, counts in object_counts.items():
        chart_path = f"../outputs/{video_name}_bar_chart.png"
        st.markdown(f"**📌 {video_name}**")
        cols = st.columns(2)
        with cols[0]:
            if os.path.exists(chart_path):
                st.image(chart_path, use_container_width=True, caption="Object Count Chart")
        with cols[1]:
            st.json(counts)
else:
    st.warning("Object count data not found. Run `analyse_objects.py` first.")

