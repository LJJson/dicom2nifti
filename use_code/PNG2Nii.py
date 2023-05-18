# 将超声的dcm格式转化成标准化的nii.gz用于Monai的使用
# 可用于讲mask转为nii 格式 2023-3-1

import os
from PIL import Image
import numpy as np
import SimpleITK as sitk
import pydicom
import skimage.transform as skTrans


def dcm2nii(dcms_path, nii_path):
    # 1.构建dicom序列文件阅读器，并执行（即将dicom序列文件“打包整合”）
    # reader = sitk.ImageSeriesReader()
    # dicom_names = reader.GetGDCMSeriesFileNames(dcms_path)
    # reader.SetFileNames(dicom_names)
    # image2 = reader.Execute()
    image2 = pydicom.read_file(dcms_path)
    image_array = image2.pixel_array
    # 2.将整合后的数据转为array，并获取dicom文件基本信息
    image_array = image_array / 255
    # 3.将array转为img，并保存为.nii.gz
    image3 = skTrans.resize(image_array, (228, 362, 362), order=1, preserve_range=True)
    image3 = sitk.GetImageFromArray(image3)

    sitk.WriteImage(image3, nii_path)


def img2nii(dcm_path, png_path, nii_path):
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dcm_path)
    reader.SetFileNames(dicom_names)
    image2 = reader.Execute()


    origin = image2.GetOrigin()  # x, y, z
    spacing = image2.GetSpacing()  # x, y, z
    direction = image2.GetDirection()  # x, y, z
    list =[]

    imgs = []
    for file_name in dicom_names:
        str2 = file_name.split("\\")[1].strip('.dcm')
        str2 = png_path+'/'+str2+".bmp" #
        list.append(str2)

    # list.reverse()
    # 获取dicom对应得尺寸
    ds = pydicom.dcmread(dicom_names[0])
    dicomshape = ds.pixel_array.shape

    for a in list:

        image = Image.open(a)
        img = np.array(image)
        img = img / 255
        img = skTrans.resize(img, dicomshape, order=1, preserve_range=True)
        print(img.shape)
        imgs.append(img)
    # file_names = os.listdir(png_path)
    # image_arr = glob.glob(str(image_path) + str("/*"))
    # # image_arr.sort()
    sStr2 = "\\"
    # file_names.sort(key=lambda x: int(x[x.find(sStr2) + 1:-4]))
    # imgs = []
    # for file_name in file_names:
    #     image = Image.open(os.path.join(png_path, file_name))
    #     img = np.array(image)
    #     img = img / 255
    #     img = skTrans.resize(img, (384, 384), order=1, preserve_range=True)
    #     print(img.shape)
    #     imgs.append(img)
    imgnii = np.stack(imgs, axis=0)
    nii = sitk.GetImageFromArray(imgnii)
    nii.SetOrigin(origin)
    nii.SetSpacing(spacing)
    nii.SetDirection(direction)

    sitk.WriteImage(nii, nii_path)


# dcms_path = r'F:\WorkPlace\Data\0928\zhu gui fang'  # dicom序列文件所在路径
# nii_path = r'F:\WorkPlace\Data\test3.nii.gz'  # 所需.nii文件保存路径
# dcm2nii(dcms_path, nii_path)###将dicom（.dcm)文件转为nifti(.nii)文件###
# dcms_path = r'F:\WorkPlace\Data\0928\xie xi yan'  # dicom序列文件所在路径
# nii_path = r'F:\WorkPlace\Data\test4.nii.gz'  # 所需.nii文件保存路径
# dcm2nii(dcms_path, nii_path)###将dicom（.dcm)文件转为nifti(.nii)文件###


# png_path=r'F:\WorkPlace\Data\0609\MRI\MRI_Mask'
# nii_path=r'F:\WorkPlace\Data\mask.nii.gz'
# dcm_path=r'F:\WorkPlace\Data\0609\MRI\DCM'
# img2nii(dcm_path,png_path,nii_path)


# 编辑此处 11-26 实现可以使用


file = '../data/02/5_8A5B0F4DA52048249EB1891F1D10ACDD'
CM_dirs = os.listdir(file)
path = file + "_masks/neddle"
print(path)
# png_path = r"../data/01/4_3C78BBCA54E440388035F3256311D3F3_masks/neddle"
png_path = path

for m in range(1, 2, 1):
    m = str(m)

    # nii_path=r"G:\prostate_data\USMask_nii_Normalize\{}_US_dicom01.nii.gz".format(m.zfill(4))
    nii_path = "../nii_output/02_05_mask.nii.gz"
    if os.path.exists(file):
        dcms_path = file
        # nii_path=file2
        print("start")
        # dcm2nii(dcms_path, file2)
        # dcm2nii(png_path, nii_path)
        img2nii(file, png_path, nii_path)
        print("end!!!")
