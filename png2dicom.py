import glob

import numpy as np
import pydicom
from PIL import Image

# 11-24 实验可行

ds = pydicom.dcmread('mask2nifti/dicom/1.3.12.2.1107.5.2.30.27965.2018042709053733597506018.dcm')  # pre-existing dicom file
jpg_image = Image.open('./mask/1.1.bmp')  # the PNG or JPG file to be replace
b = 1
for i in glob.glob('./mask/*.bmp', recursive=True):
        jpg_image = Image.open(i)
        if jpg_image.mode == 'L':
            np_image = np.array(jpg_image.getdata(), dtype=np.uint8)
            ds.Rows = jpg_image.height
            ds.Columns = jpg_image.width
            ds.PhotometricInterpretation = "MONOCHROME1"
            ds.SamplesPerPixel = 1
            ds.BitsStored = 8
            ds.BitsAllocated = 8
            ds.HighBit = 7
            ds.PixelRepresentation = 0
            ds.PixelData = np_image.tobytes()
            ds.save_as('./png2nifti/1.3.12.2.1107.5.2.30.27965.201804270905372962430601{}.dcm'.format(b))
            b += 1

        elif jpg_image.mode == 'RGBA':

            np_image = np.array(jpg_image.getdata(), dtype=np.uint8)[:, :3]
            ds.Rows = jpg_image.height
            ds.Columns = jpg_image.width
            ds.PhotometricInterpretation = "RGB"
            ds.SamplesPerPixel = 3
            ds.BitsStored = 8
            ds.BitsAllocated = 8
            ds.HighBit = 7
            ds.PixelRepresentation = 0
            ds.PixelData = np_image.tobytes()
            ds.save_as('result_rgb.dcm')
