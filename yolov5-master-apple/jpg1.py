# 以tiff转jpg为例，其他格式同理，
# 代码中路径更改为自己图像存放路径即可

import os
import cv2 as cv2

imagesDirectory = r"D:\yolov5-master\pictures\oldpng"  # tiff图片所在文件夹路径
distDirectory = os.path.dirname(imagesDirectory)  #

distDirectory = os.path.join(distDirectory, "newjpj")  # 要存放bmp格式的文件夹路径
print(distDirectory)

for imageName in os.listdir(imagesDirectory):
    print("imageName", imageName)
    imagePath = os.path.join(imagesDirectory, imageName)
    print("imagePath", imagePath)
    img = cv2.imread(imagePath)
    try:
        img.shape
    except:
        print('读取图片失败')
        break

    print("imageName.split('.')[0]", imageName.split('.')[0])
    distImagePath = os.path.join(distDirectory, imageName.split('.')[0] + '.jpg')  # 更改图像后缀为.jpg，并保证与原图像同名
    print("distImagePath", distImagePath)
    cv2.imwrite(distImagePath, img)