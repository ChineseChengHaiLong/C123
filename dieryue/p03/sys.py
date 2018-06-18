import sys
import time
class People:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
class Daitu:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
xiaoming=People('小明','20')
xiaohua=Daitu('小花','15')
time.sleep(2)
print(xiaoming.name)
print(sys.getrefcount(xiaoming))
print(xiaohua.name)
print(sys.getrefcount(xiaohua))
print(isinstance(xiaoming,People))
print(isinstance(xiaohua,Daitu))
