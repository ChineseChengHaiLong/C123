import time
class Qiche(object):
    def lun_zi(self):
        print('车有四个轮子。。。')
    def pao(self):
        time.sleep (1)
        print('3')
        time.sleep (1)
        print('2')
        time.sleep (1)
        print('1')
        print('能跑，还跑得特快。。。')
    def sha_che(self):
        print('能刹车，立马刹车。。。')
class baoma(Qiche):
    def chang(self):
        print('宝马车长4.6米')
    def weizhi(self):
        print('宝马车有5个座位')
    def mali(self):
        print('宝马车马力500匹')
    def changdu(self):
        print('奔驰车长5.2米')
    def wei(self):
        print('奔驰有5个座位')
    def liqi(self):
        print('奔驰马力600匹')
class mai1: 
#    def __init__(self):
 #       super().maijia(self)
  #      super().mai(self)    
    def maimai(self,che):
        if che == '宝马':
            print('宝马卖价100W')
        elif che == '奔驰': 
            print('奔驰要价101W')
print('欢迎来到汽车服务')
che = baoma()
car=input('请输入您要查看要的汽车名字：宝马、奔驰')
if car == '宝马':
    che.chang()
    che.weizhi()
    che.mali()
    che.lun_zi()
    che.pao()
    che.sha_che()
elif car == '奔驰':
    che.changdu()
    che.wei()
    che.liqi()
    che.lun_zi()
    che.pao()
    che.sha_che()
che1=mai1()
car1=input('请输入您要查寻的车价: 宝马、奔驰')
che1.maimai(car1)
