from ultralytics import YOLO

# 加载训练好的最佳模型（请根据实际路径修改）
model_path = "runs/detect/eval_yolo/yolov8n/weights/best.pt"
model = YOLO(model_path)

# 导出为 ONNX 格式，使用半精度（FP16）
model.export(format="onnx", half=True)
