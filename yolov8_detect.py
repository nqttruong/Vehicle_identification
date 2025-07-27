from networkx.algorithms.flow import build_residual_network
from ultralytics import YOLO
import cv2
import os

def detect_video(video_path, output_path, model_path='/media/truong/01DBB45ECE0C4E00/dl/nhan_dien_xe/runs/detect/train2/weights/best.pt', conf=0.4):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=conf)[0]
        annotated_frame = results.plot()
        out.write(annotated_frame)

    cap.release()
    out.release()

    return output_path















