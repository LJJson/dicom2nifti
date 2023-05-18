import SimpleITK as sitk
import glob
import numpy as np
import cv2
import os
from PIL import  Image



# 没有和dicom 对应
# 2023-2-28


import matplotlib.pyplot as plt  # plt 用于显示图片


def save_array_as_nii_volume(data, filename, reference_name=None):
    """
    save a numpy array as nifty image
    inputs:
        data: a numpy array with shape [Depth, Height, Width]
        filename: the ouput file name
        reference_name: file name of the reference image of which affine and header are used
    outputs: None
    """
    img = sitk.GetImageFromArray(data)
    if (reference_name is not None):
        img_ref = sitk.ReadImage(reference_name)
        img.CopyInformation(img_ref)


    sitk.WriteImage(img, filename)


file = r"png2nifti"

file2 = "./nii_output"
file3 = "./png2nifti"

US_dirs = os.listdir(file)
print(len(US_dirs))

for m in range(11, 21, 1):
    m = str(m)
    # image_path = r'./mask2nifti/new/1.3.12.2.1107.5.2.30.27965.20180427090537296243060{}'.format(m)
    image_path = r'data/4_579E62D1A4D3455DA93951801FA6F03A_masks/neddle'

    if os.path.exists(image_path):
        US_dirs2 = os.listdir(image_path)
        image_arr = glob.glob(str(image_path) + str("/*"))
        # image_arr = glob.glob(str(image_path))

        image_arr.sort()

        print(image_arr, len(image_arr))

        # count=0
        # for n in range(0, len(US_dirs2), 1):
        #     count=count+1
        # print(count)
        for i in image_arr:
            img = Image.open(i)
            w = img.width
            h = img.height

        allImg = []
        allImg = np.zeros([len(image_arr), h, w], dtype='uint8')
        for i in range(len(image_arr)):
            single_image_name = image_arr[i]
            img_as_img = Image.open(single_image_name)
            # img_as_img.show()

            img_as_np = np.asarray(img_as_img)
            allImg[i:, :, ] = img_as_np
        # allImg = allImg / 255
        # allImg = skTrans.resize(allImg, (228, 362, 362), order=1, preserve_range=True)
        # np.transpose(allImg,[2,0,1])
        if not os.path.exists(file2):
            os.makedirs(file2)
        save_array_as_nii_volume(allImg, 'nii_output/{}_US_dicom03.nii.gz'.format(m.zfill(4)))
        print(np.shape(allImg))
        img = allImg[:, :, 55]
        # plt.imshow(img, cmap='gray')
        # plt.show()