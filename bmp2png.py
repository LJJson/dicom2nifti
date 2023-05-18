import glob
import os
from PIL import Image

newpath = "mask2nifti/new"

for i in glob.glob('./mask2nifti/pubis/*.bmp', recursive=True):
    print(i)
    img = Image.open(i)
    path1 = os.path.split(i)[0]
    path2 = os.path.split(i)[1].replace("bmp", "png")
    new_path = os.path.join(newpath, path2)
    img.save(new_path)
