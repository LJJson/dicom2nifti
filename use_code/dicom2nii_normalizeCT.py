#将以文件命名的cdm序列转换成标准化后的nii.gz格式用于Monai的运行 2023-3-1
from PIL import Image
import numpy as np
import SimpleITK as sitk
import  os
def dcm2nii(dcms_path, nii_path):
    # 1.构建dicom序列文件阅读器，并执行（即将dicom序列文件“打包整合”）
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dcms_path)
    reader.SetFileNames(dicom_names)
    image2 = reader.Execute()
    # print(image2)
    # 2.将整合后的数据转为array，并获取dicom文件基本信息
    image_array = sitk.GetArrayFromImage(image2)  # z, y, x
    image_array = image_array/255
    origin = image2.GetOrigin()  # x, y, z
    spacing = image2.GetSpacing()  # x, y, z
    direction = image2.GetDirection()  # x, y, z
    # 3.将array转为img，并保存为.nii.gz
    image3 = sitk.GetImageFromArray(image_array)
    image3.SetSpacing(spacing)
    image3.SetDirection(direction)
    image3.SetOrigin(origin)
    sitk.WriteImage(image3, nii_path)


# file1 = "../data/01/3_E481B6366FA74596B111E93E5828875F"
# file2 = "../data/02/3_528A6F5ABE8441F5BE871E82CDA4C732"
# file3 = "../data/02/4_33833525EB424011A0853094CA298134"
# file4 = "../data/02/5_8A5B0F4DA52048249EB1891F1D10ACDD"
# file5 = "../data/02/6_5CBADC33962C44CF83CF84A8125A8FC"
# file6 = "../data/01/7_DCDBA7C68904528A7E85272AADB772C"

# file1 = "../data/02/2_CBFA903A8FD4C94B662AB2D69973DB"
# file2 = "../data/02/3_528A6F5ABE8441F5BE871E82CDA4C732"
# file3 = "../data/02/4_33833525EB424011A0853094CA298134"
# file4 = "../data/02/5_8A5B0F4DA52048249EB1891F1D10ACDD"
# file5 = "../data/02/6_5CBADC33962C44CF83CF84A8125A8FC"
# file6 = "../data/02/7_55AC2A5F9AD148789C39191362C69884"



# file1 = "../data/03/3_315344D89C8A401ABAD0E3FB1614C14D"
# file2 = "../data/03/4_CBD3912148514316BB8A84749789AA8B"
# file3 = "../data/03/5_F2B8D7B981584498A16DDAA62513CA"
# file4 = "../data/03/6_414AB673F9514F5C9D809272C9E6A3DB"
# file5 = "../data/03/7_E7B3DE14EAA04641BBB45580C7FD2722"
#
#
#

# file1 = "../data/04/3_1_105BE5AD63E143729897FDE0B3F65564"
# file2 = "../data/04/3_60A0366591474996A5879B502259A8F"
# file3 = "../data/04/4_1_630FD9C98DEF440FB12096B7A68E33B6"
# file4 = "../data/04/4_98234A0068D548B590F3C44E56380C2"
# file5 = "../data/04/5_1_91281FB362B04CAF9280E77C854BEE5B"
# file6 = "../data/04/5_DF12FC611370437AB0ECDADBB1C7E89"
# file7 = "../data/04/6_1_F5FED4EA984347F9AA996E8272FED46"
# file8 = "../data/04/6_D87B0FAD836946B6B025CCAA85CB6391"
# file9 = "../data/04/7_1_273136EE2E094BBFBD462423167DBBC"
# file10 = "../data/04/7_91EE2C7DBD7D464A83E74B508E26C43B"

file1 = "../data/prostate/252429000_t2_tse_sag_384_p2"
file2 = "../data/prostate/353019000_t2_tse_cor_384_p2"
file3 = "../data/prostate/453155000_t2_tse_tra_384_p2"


output = '../nii_output/453155000_t2_tse_tra_384_p2.nii.gz'


dcm2nii(file3, output)
source_image = sitk.ReadImage(output)
print(source_image.GetSize())
print("完成！！")
