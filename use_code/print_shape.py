import SimpleITK as sitk
import os
import numpy as np

import pydicom
#
# ds=pydicom.dcmread()
# ds.bit
path = os.listdir('../data_test')

str1 = "../data_test/pre2_label.nii.gz"
for read_path in path:
    str = '../data_test/'+read_path

    print(str)
    source_image = sitk.ReadImage(str1)

    nda = sitk.GetArrayFromImage(source_image)
    ab = np.sum(abs(nda))
    # print(nda)
    print(type(source_image))
    print(source_image.GetSize())
    print("\n")
    # new_size = [256, 256, 30]
    # resampled_image = sitk.Resample(source_image, new_size)
    # sitk.WriteImage(resampled_image, "../nii_output/STA.nii.gz")



