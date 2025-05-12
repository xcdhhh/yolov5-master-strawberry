# from PIL import Image
#
#
# def clamp_rgb(value):
#     return max(0, min(255, value))
#
#
# def limit_image_rgb(image_path):
#     # Open an image file
#     img = Image.open(image_path)
#
#     # Convert image to RGB mode (ignores alpha channel if present)
#     img = img.convert('RGB')
#
#     # Process each pixel
#     width, height = img.size
#     pixels = img.load()
#     for y in range(height):
#         for x in range(width):
#             # Get RGB values of the pixel
#             r, g, b = pixels[x, y]
#
#             # Clamp RGB values
#             r = clamp_rgb(r)
#             g = clamp_rgb(g)
#             b = clamp_rgb(b)
#
#             # Update pixel with clamped values
#             pixels[x, y] = (r, g, b)
#
#     # Save modified image
#     img.save("clamped_image.jpg")
#
#
# # Example usage:
# limit_image_rgb(r"D:\打工文件\yolov5-master-apple\yolov5-master-apple\background\background.jpg")
from PIL import Image
import os

def resize_images(input_dir, output_dir, size):
    # 如果输出目录不存在，则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # 可以根据需要扩展
            # 构建输入和输出文件的完整路径
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # 打开并调整图像大小
            original_image = Image.open(input_path)
            resized_image = original_image.resize(size)
            resized_image.save(output_path)

# 示例用法
input_directory = '6-caomei/6-caomei/images/valid/'  # 输入图像所在的文件夹
output_directory = '6-caomei/6-caomei/images/valid1/'  # 调整大小后的图像输出文件夹
target_size = (700, 500)  # 目标大小

resize_images(input_directory, output_directory, target_size)

