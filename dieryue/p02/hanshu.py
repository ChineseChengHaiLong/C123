import os
import shutil
a=input('请输入您要创建的文件夹：')
os.mkdir(a)
b=os.getcwd()
print(b)
b=input('请输入您要删除的文件夹名字：')
shutil.rmtree(b)
c=os.listdir('./')
print(c)


