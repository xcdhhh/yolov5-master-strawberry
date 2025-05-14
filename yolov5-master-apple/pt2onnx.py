import torch
import onnx
from models.experimental import attempt_load
# 加载Yolov5模型
model = attempt_load(r"D:\打工文件\yolov5-master-apple\yolov5-master-apple\runs\train\exp40\weights\best.pt")
# 准备输入数据
dummy_input = torch.randn(1, 3, 640, 640)
# 导出为ONNX格式，指定opset版本为11
export_path = 'yolov5s.onnx'
torch.onnx.export(model, dummy_input, export_path, opset_version=11)
#验证
# onnx_model = onnx.load(export_path)
# onnx.checker.check_model(onnx_model)
# print('ONNX model is valid.')