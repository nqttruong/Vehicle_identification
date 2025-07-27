import streamlit as st
from yolov8_detect import detect_video
import os
import uuid

st.set_page_config(page_title="Detect use YOLOV8", layout="centered")

st.title("Detect in video")
uploaded_file = st.file_uploader("Upload video MP4", type=["mp4"])

if uploaded_file:
    video_id = str(uuid.uuid4())
    input_video_path = f"temp_input_{video_id}.mp4"
    output_video_path = f"temp_output_{video_id}.mp4"

    with open(input_video_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("processing video ..."):
        detect_video = (input_video_path, output_video_path)

    st.success("processed")
    st.video(output_video_path)