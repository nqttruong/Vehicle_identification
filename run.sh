#yolo train model=yolov8n.yaml \
#		data=/media/truong/01DBB45ECE0C4E00/dl/nhan_dien_xe/giao_thong.v1i.yolov8-obb/data.yaml \
#		epochs=100 imgsz=1080 batch=2\
#		project=nhan_dien_xe name=checkpoint


yolo train model=/media/truong/01DBB45ECE0C4E00/dl/nhan_dien_xe/runs/detect/train/weights/best.pt \
             data=/media/truong/01DBB45ECE0C4E00/dl/nhan_dien_xe/giao_thong.v1i.yolov8-obb/data.yaml \
             epochs=100 imgsz=2048 batch=2

