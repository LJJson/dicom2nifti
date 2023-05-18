import os
import re


def changename(orignname):
    picture = os.listdir(orignname)
    for filename in picture:
        # filename1 = filename.split(".")[0]
        # filename2=re.findall(r"\d+\.?\d*", filename1)[0]+".png"
        # srcpath = os.path.join(orignname,filename)
        # allpath = os.path.join(orignname,filename2)
        # os.rename(srcpath,allpath)

        # split("_",2)[1]    “_”表示分隔符 ; 2表示分割次数 ; [1]表示选取第 i 个片段
        filename1 = filename.split("_")[3]
        # 设置旧文件名（就是路径+文件名）
        srcpath = os.path.join(orignname, filename)
        # 设置新文件名
        allpath = os.path.join(orignname, filename1)
        os.rename(srcpath, allpath)


if __name__ == '__main__':
    orignname = r"D:\AK\GJ\dataset_2\val\labels"
    changename(orignname)