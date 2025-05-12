import torch
import onnx
from models.experimental import attempt_load

# 加载Yolov5模型
model = attempt_load(r"D:\打工文件\yolov5-master-apple\yolov5-master-apple\runs\train\exp40\weights\best.pt")
model.eval()  # 设置为评估模式

# 准备输入数据
dummy_input = torch.randn(1, 3, 640, 640)

# 导出为ONNX格式，指定opset版本为11
export_path = 'yolov5s.onnx'

# 导出模型并添加动态轴支持
torch.onnx.export(
    model,
    dummy_input,
    export_path,
    opset_version=11,
    input_names=['images'],  # 输入名称
    output_names=['output'],  # 输出名称
    dynamic_axes={
        'images': {0: 'batch', 2: 'height', 3: 'width'},  # 动态输入维度
        'output': {0: 'batch', 1: 'anchors'}  # 动态输出维度
    },
    do_constant_folding=False,  # 禁用常量折叠以保留条件逻辑
    verbose=False  # 设置为True可查看详细导出过程
)

# 验证导出的ONNX模型
try:
    onnx_model = onnx.load(export_path)
    onnx.checker.check_model(onnx_model)
    print('ONNX模型验证通过!')
except Exception as e:
    print(f'ONNX模型验证失败: {e}')