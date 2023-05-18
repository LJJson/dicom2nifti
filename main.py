# import glob
# import os
# from PIL import Image
#
# for i in glob.glob('./mask2nifti/pubis/*.bmp', recursive=True):
#     print(i)
#     img = Image.open(i)
#     path1 = os.path.split(i)[0]
#     path2 = os.path.split(i)[1].replace("bmp", "png")
#     new_path = os.path.join(path1,path2)
#     img.save(new_path)
# 12-3使用正常
# import dicom2nifti
#
# dicom_directory = "data/03/4_CBD3912148514316BB8A84749789AA8B"
# dicom_directory_2 = "data/03/5_F2B8D7B981584498A16DDAA62513CA"
# dicom_directory_3 = "data/03/6_414AB673F9514F5C9D809272C9E6A3DB"
# dicom_directory_4 = 'data/03/7_E7B3DE14EAA04641BBB45580C7FD2722'
# dicom_directory_5 = "D:/Slicer 5.2.1/output/5"
# dicom_directory_6 = 'data/1_9F105CE3F97A4B08ADE92BC055B03C9B'
#
# output_folder = "output"
#
# dicom2nifti.convert_directory(dicom_directory, output_folder, compression=True, reorient=True)

import SimpleITK as sitk
import numpy as np

path = "./nii_output/01_03.nii.gz"
path1 = "./nii_output/01_04.nii.gz"
img = sitk.ReadImage(path)
nda = sitk.GetArrayFromImage(img)
print("nda_shape: ")
print(nda.shape)
x = nda.flatten().astype('double')
print(x.shape)

img1 = sitk.ReadImage(path1)
nda1 = sitk.GetArrayFromImage(img1)
print("nda1_shape: ")
print(nda1.shape)
y = nda1.flatten().astype('double')
c1 = x.dot(y) / x.dot(x)

print(c1)


