import cv2
import numpy as np

# 读取图像
img = cv2.imread('image.jpg')

# 加载LapSRN模型
model = cv2.dnn.readNet('LapSRN_x4.pb')

# 将图像转换为blob格式
blob = cv2.dnn.blobFromImage(img, 1.0 / 255.0, (img.shape[1], img.shape[0]), (0, 0, 0), swapRB=False, crop=False)

# 设置输入和输出节点的名称
input_node = 'input'
output_node = 'output'

# 设置输入blob
model.setInput(blob, input_node)

# 运行模型，获取输出blob
output_blob = model.forward(output_node)

# 将输出blob转换为图像
output_img = (np.clip(output_blob[0], 0, 1) * 255).astype(np.uint8)
output_img = output_img.transpose(1, 2, 0)

# 显示原始图像和输出图像
cv2.imshow('Input', img)
cv2.imshow('Output', output_img)
cv2.waitKey(0)