import cv2
import nibabel as nib
import numpy as np

#
# if __name__ == '__main__':
#     volume_path = '../data/mask_dicom/Shoulder_4_mask.nii.gz'
#     img_path = 'volume.png'
#     volume = nib.load(volume_path)
#     img = volume.get_fdata().squeeze()
#     img = img.transpose([1, 0])
#     img = np.flip(img, 0)
#     img = np.flip(img, 1)
#     cv2.imwrite(img_path, img)

import SimpleITK as sitk
import os
import cv2


def nii2png_single(nii_path, IsData = True):
    ori_data = sitk.ReadImage(nii_path)  # 读取一个数据
    data1 = sitk.GetArrayFromImage(ori_data)  # 获取数据的array
    if IsData:  #过滤掉其他无关的组织，标签不需要这步骤
        data1[data1 > 250] = 250
        data1[data1 < -250] = -250
    img_name = os.path.split(nii_path)  #分离文件名
    img_name = img_name[-1]
    img_name = img_name.split('.')
    img_name = img_name[0]
    i = data1.shape[0]
    png_path = '../nii_output'   #图片保存位置
    if not os.path.exists(png_path):
        os.makedirs(png_path)
    for j in range(0, i):   #将每一张切片都转为png
        if IsData:  # 数据
            #归一化

            slice_i = (data1[j, :, :] - data1[j, :, :].min()) / (data1[j, :, :].max() - data1[j, :, :].min()) * 255
            cv2.imwrite("%s/%s-%d.png" % (png_path, img_name, j), slice_i)  #保存
        else:   # 标签
            slice_i = data1[j, :, :] * 122
            cv2.imwrite("%s/%s-%d.png" % (png_path, img_name, j), slice_i)  # 保存


volume_path = '../data/mask_dicom/reconstruction568.nii.gz'
nii2png_single(volume_path,False)