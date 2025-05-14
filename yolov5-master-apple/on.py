# coding=utf-8
import torch
from models.experimental import attempt_load

def convert_pth_to_onnx(pth_path, onnx_path, num_cls=4):
    # 强制使用CPU设备以避免设备不一致问题
    device = torch.device("cpu")
    # 加载模型到指定设备
    model = attempt_load(pth_path, map_location=device)
    model.to(device)  # 确保整个模型转移到设备
    model.eval()

    # 创建虚拟输入并确保其在同一设备
    dummy_input = torch.randn(1, 3, 640, 640, device=device)

    # 设置动态轴（根据模型实际输出调整）
    dynamic_axes = {
        'input': {0: 'batch_size'},  # 仅批次维度动态
        'output': {0: 'batch_size'}
    }

    # 导出ONNX模型
    torch.onnx.export(
        model,
        dummy_input,
        onnx_path,
        export_params=True,
        input_names=["input"],
        output_names=["output"],
        opset_version=12,  # 使用更高的OP版本
        dynamic_axes=dynamic_axes,
        do_constant_folding=True,
        training=torch.onnx.TrainingMode.EVAL,
        verbose=False
    )
    print(f"成功导出ONNX模型至: {onnx_path}")

if __name__ == "__main__":
    pth_file = r"D:\打工文件\yolov5-master-apple\yolov5-master-apple\runs\train\exp40\weights\best.pt"
    onnx_file = "./model_last.onnx"
    convert_pth_to_onnx(pth_file, onnx_file)