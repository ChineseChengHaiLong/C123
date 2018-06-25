import pygame
class Plane(object):
    def __init__(self,ing_path,chuangkou,x,y):
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.chuangkou=chuangkou#游戏窗口
        self.ing_path=ing_path#飞机路径
        self.Feiphoto = pygame.image.load(self.ing_path)#飞机图获取代码中，背景
        self.Feiweizhi = pygame.Rect(self.x,self.y,self.w,self.h)#飞机的位置
        self.bullet_list=[]# 定义子弹的保存列表
    def display(self):    
        self.chuangkou.blit(self.Feiphoto,self.Feiweizhi)
        for i in self.bullet_list:  #显示子弹
            if i.judge():
                self.bullet_list.remove(i)
            i.weizhi()  #子弹的对像.weizhi()
            i.move()
class Tullet(object):
    def __init__(self,ing_path,chuangkou,x,y):
        self.x=x
        self.y=y
        self.chuangkou=chuangkou#游戏窗口
        self.ing_path=ing_path#子弹路径
         
        self.bulletphoto = pygame.image.load(self.ing_path)#子弹图获取代码中，背景
    def weizhi(self):#定义把子弹图加载到窗口上并定义位置
        self.chuangkou.blit(self.bulletphoto,(self.x,self.y))
