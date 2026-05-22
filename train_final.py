from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="dataset/data.yaml", epochs=150, imgsz=640, batch=8,
            mosaic=1.0, mixup=0.2, copy_paste=0.2, degrees=10, scale=0.8,
            cos_lr=True, lrf=0.01, label_smoothing=0.1,
            project="eval_yolo", name="yolov8n")
