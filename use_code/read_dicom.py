import pydicom

filepath = "../data/mask_dicom/1.3.12.2.1107.5.2.30.27965.2018042709053729624306013.dcm"
data = pydicom.dcmread(filepath + '')  # 读取一张dcm文件\
print(data.data_element)

# image_path = './mask'
# image_arr = glob.glob(str(image_path) + str("/*"))
# # image_arr.sort()
# sStr2 = "\\"
# image_arr.sort(key=lambda x: int(x[x.find(sStr2) + 1:-4]))
