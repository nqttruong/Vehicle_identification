import streamlit as st
from yolov8_detect import detect_video
import os
import uuid
import subprocess

st.set_page_config(page_title="Detect use YOLOv8", layout="centered")

st.title("Detect in video")
uploaded_file = st.file_uploader("Upload video MP4", type=["mp4"])

if uploaded_file:
    video_id = str(uuid.uuid4())
    input_video_path = f"temp_input_{video_id}.mp4"
    raw_output_path = f"temp_output_raw_{video_id}.mp4"
    converted_output_path = f"temp_output_{video_id}.mp4"

    # Save uploaded file
    with open(input_video_path, "wb") as f:
        f.write(uploaded_file.read())

    # Call actual detection function
    with st.spinner("🚀 Processing video..."):
        detect_video(input_video_path, raw_output_path)

        # Convert to H.264 + AAC format
        subprocess.run([
            "ffmpeg", "-y", "-i", raw_output_path,
            "-vcodec", "libx264", "-acodec", "aac",
            converted_output_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Check output file exists
    if os.path.exists(converted_output_path):
        st.success("✅ Video processed and converted successfully!")
        st.video(converted_output_path)
    else:
        st.error("❌ Failed to generate output video.")
