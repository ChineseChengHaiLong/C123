import pygame  #导入pygame包
import random
from p import *

class Enemyplane(Plane):   #创建飞机类
    #初始值飞机图片路径、游戏窗口
    def __init__(self,ing_path,chuangkou):
        Plane.__init__(self,ing_path,chuangkou,0,0)
        self.flag = 'right'
    def move(self):#定义move方法使敌机左右移动
        if self.flag == 'right':
            self.Feiweizhi.x += 2
        else:
            self.Feiweizhi.x -= 2
 
        if self.Feiweizhi.x > 400 - self.Feiweizhi.width:
            self.flag = 'left'
        elif self.Feiweizhi.x <= 0:
            self.flag = 'right'


     # 发射子弹
    def fire(self):
        a = Dizidan('./images/bullet1.png',self.chuangkou,self.Feiweizhi.x,self.Feiweizhi.y)#定义子弹的对象
        self.bullet_list.append(a)#把子弹追加到子弹列表中
    def fire1(self):
        a = Dizidan('./images/bullet1.png',self.chuangkou,self.Feiweizhi.x+70,self.Feiweizhi.y)#定义子弹的对象
        self.bullet_list.append(a)#把子弹追加到子弹列表中
class Dizidan(Tullet):   #创建子弹类
    #初始值子弹图片路径、游戏窗口
    def move(self):
        self.y += 6
    def judge(self):#判断子弹是否跑出屏幕外
        if self.y > 600:
            return True #表示子弹飞出屏幕
        else:
            return False
class Feiji(Plane):
    #初始值飞机图片路径、游戏窗口
    def __init__(self,ing_path,chuangkou):
        Plane.__init__(self,ing_path,chuangkou,(400-100)/2,350)
        self.bao_list=[]
        self.panduanbao = False
        self.baotu()
        self.a =0
        self.b =0
     # 发射子弹
    def fire(self):
        a = Zidan('./images/plane.png',self.chuangkou,self.Feiweizhi.x,self.Feiweizhi.y)#定义子弹的对象发出子弹就把他放到列表中
        self.bullet_list.append(a)#把子弹追加到子弹列表中

    def fire1(self):
        a = Zidan('./images/plane.png',self.chuangkou,self.Feiweizhi.x+70,self.Feiweizhi.y)#定义子弹的对象
        self.bullet_list.append(a)#把子弹追加到子弹列表中
    def baozha(self):
        self.panduanbao = True
    def baotu(self):
        u = pygame.image.load('./images/hero_blowup_n1.png')
        self.bao_list.append(u)
        i = pygame.image.load('./images/hero_blowup_n2.png')
        self.bao_list.append(i)
        p = pygame.image.load('./images/hero_blowup_n3.png')
        self.bao_list.append(p)
        y = pygame.image.load('./images/hero_blowup_n4.png')
        self.bao_list.append(y)
    def baohuan(self):
        if self.panduanbao == True:
            self.chuangkou.blit(self.bao_list[self.a],self.Feiweizhi)
            self.b+=1
            if self.b == 10:
                self.a+=1
                self.b = 0
            if self.a > 3:
                self.Feiweizhi.x = 500
                self.Feiweizhi.y = 800
                exit()              
class Zidan(Tullet):   #创建子弹类
    #初始值子弹图片路径、游戏窗口
    def move(self):
        self.y -= 6
    def judge(self):#判断子弹是否跑出屏幕外
        if self.y < 5:
            return True #表示子弹飞出屏幕
        else:
            return False
def jianshi(hero,move):
        for i in pygame.event.get():#游戏事件的监听，控制
            if i.type == pygame.QUIT:#如果某一操作等于退出
                print('退出程序')
                pygame.quit()#退出程序
                exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    hero.fire()
                    hero.fire1()
                elif i.key == pygame.K_z:
                    hero.baozha()                   
        keys = pygame.key.get_pressed()
       # if keys[pygame.K_SPACE]or keys[pygame.K_x]:
        #    hero.fire()
         #   hero.fire1()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if hero.Feiweizhi.x < 400 - hero.Feiweizhi.width:
                hero.Feiweizhi.x += move
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if hero.Feiweizhi.x > 0:
                hero.Feiweizhi.x -= move
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if hero.Feiweizhi.y < 700 - hero.Feiweizhi.height:
                hero.Feiweizhi.y += move
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if hero.Feiweizhi.y > 0:
                hero.Feiweizhi.y -= move
def feiji():#创建函数
    chuangkou = pygame.display.set_mode((400,700),0,32)#定义游戏窗口大小
    beijing = pygame.image.load('./images/background.png')#把背景图获取代码中
    clock = pygame.time.Clock()#pygame中自带的时间包
    hero = Feiji('./images/hero1.png',chuangkou)#创建一个飞机对象，传入路径参数
    
    hero1 = Enemyplane('./images/enemy1.png',chuangkou)    
    while True: #循环输出
        jianshi(hero,10)
        chuangkou.blit(beijing,(0,0))#打背景图获取到代码上
        hero.display()#对象调用类属性，把飞机图获取到代码上并定义位置
        hero.baohuan()
        hero1.display()
        hero1.move()#调用move方法移动
        num = random.randint(1,50)
        if num == 11:
            hero1.fire()
            hero1.fire1()
        pygame.display.update()#刷新显示
       # clock.tick(60)#每隔多少秒运行一下
if __name__ == '__main__':#有权限的访问，只有自己可以调式，其他人调用不显示
    feiji()
