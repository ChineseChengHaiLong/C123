import pygame
import time
import random
from random import randint
pygame.init()
class Plane(object):#飞机的父类
    def __init__(self,lujing,screen,x,y):

        self.lujing=lujing
        self.screen=screen
        self.x=x
        self.y=y
        self.width=22
        self.height=22
        self.feiji1=pygame.image.load(self.lujing)
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.flag="right"
        self.bulletlist=[]
        self.score=0
    def display(self):
        self.screen.blit(self.feiji1,self.rect)
        for i in self.bulletlist:
            if i.xiaoshi():
                self.bulletlist.remove(i)

            i.display()
            i.mv()


class Zidan(object):#子弹的父类
    def __init__(self,lujing,screen,x,y):
        self.lujing=lujing
        self.screen=screen
        self.x=x+34
        self.y=y
        self.bullet=pygame.image.load(self.lujing)
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))

class HeroPlane(Plane):#英雄的飞机
    def __init__(self,lujing,screen,x,y):
        Plane.__init__(self,lujing,screen,x,y)
        self.baolist=[]
        self.baotian()
        self.a=0
        self.b=0

        self.shifoubao=False
    def fire(self):
        self.bulletlist.append( Bullet("./images/plane.png",self.screen,self.rect.x,self.rect.y))
    def baotian(self):
        self.baolist.append(pygame.image.load("./images/hero_blowup_n1.png"))
        self.baolist.append(pygame.image.load("./images/hero_blowup_n2.png"))
        self.baolist.append(pygame.image.load("./images/hero_blowup_n3.png"))
        self.baolist.append(pygame.image.load("./images/hero_blowup_n4.png"))
    def baozha(self):
        self.shifoubao=True

    def panzha(self):
        if self.shifoubao==True:
            self.screen.blit(self.baolist[self.a],self.rect)
            self.b+=1
            if self.b==1:
                self.a+=1
                self.b=0
            if self.a>3:
                self.a=0
                self.rect.x=100
                self.rect.y=378

        #else:
         #self.screen.blit(self.lujing,self.rect)

class EnemyPlane(Plane):    #敌人的飞机
    def __init__(self,lujing,screen,x,y):
        Plane.__init__(self,lujing,screen,x,y)
        self.baolist=[]

        self.shifoubao=False
        self.baotian()
        self.a=0
        self.b=0
        self.shanchu="y"


    #def duojiao(self):
     #   self.screen.
    def fire(self):
        self.bulletlist.append(dBullet("./images/bullet1.png",self.screen,self.rect.x,self.rect.y+39))

    def baotian(self):
        self.baolist.append(pygame.image.load("./images/enemy0_down1.png"))
        self.baolist.append(pygame.image.load("./images/enemy0_down2.png"))
        self.baolist.append(pygame.image.load("./images/enemy0_down3.png"))
        self.baolist.append(pygame.image.load("./images/enemy0_down4.png"))
    def panzha(self,hero):
        if self.shifoubao==True:
            self.screen.blit(self.baolist[self.b],self.rect)
            self.a+=1
            if self.a==1:
                self.b+=1
                self.a=0
            if self.b>3:
                self.b=0
                self.shanchu="n"
                hero.score+=100
                self.rect.x=600
                self.rect.y=600
    def baozha(self):
        self.shifoubao=True

    def move1(self):
        if self.flag=="right":
            self.rect.x+=3
            self.rect.y+=2

        else :
            self.rect.x-=3
            self.rect.y+=3
        if self.rect.x>320:
            #if self.rect.y<=0:
                #self.rect.y+=40
            self.rect.y+=9
            self.flag="left"
        elif self.rect.x<0:
           # if self.rect.y<=0:
                #self.rect.y+=20
            self.rect.y+=9
            self.flag="right"
class Bullet(Zidan):#英雄的子弹
    def __init__(self,lujing,screen,x,y):
        Zidan.__init__(self,lujing,screen,x,y)

    def mv(self):
        self.y-=5
    def xiaoshi(self):
        if self.y<0:
            return True
        else:
            return False

class dBullet(Zidan):#敌人的子弹
    def __init__(self,lujing,screen,x,y):
        Zidan.__init__(self,lujing,screen,x,y)
    def mv(self):
        self.y+=5
    def xiaoshi(self):
        if self.y>500:
            return True
        else:
            return False
class EnemyPlane2(object):
    def __init__(self,screen):
        self.screen=screen
        self.enemylist=[]
        self.addenemyplane()
    def addenemyplane(self):
        self.enemylist.append(EnemyPlane("./images/enemy0.png",self.screen,randint(1,380),0))
    def dispp(self,hero):
        for i in self.enemylist:
            i.display()
            i.move1()
            i.shifoubao=False
            jiluo(hero,i,51,39)
            jiluo(i,hero,69,89)
            i.panzha(hero)
            aa=random.randint(1,50)
            if aa%27==0:
                i.fire()
            if i.shanchu=="n":
                self.enemylist.remove(i)
def jiluo(fa,zhui,a,b):
    for i in fa.bulletlist:
        if (i.x >= zhui.rect.x and i.x <= zhui.rect.x+a) and (i.y >= zhui.rect.y and i.y <= zhui.rect.y+b):
            zhui.baozha()
cc=pygame.USEREVENT
pygame.time.set_timer(cc,2500)
def move(move_step,hero,enemy):
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出了")
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.fire()

        if event.type==cc:
            enemy.addenemyplane()
    if keys_pressed[pygame.K_q]:
        hero.baozha()
        enemy.baozha()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x<300:
            hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x>0:
            hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y>0:
            hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y<376:
            hero.rect.y += move_step

def main():
    screen=pygame.display.set_mode((400,500),0,32)
    font=pygame.font.SysFont("arial",25)

    background=pygame.image.load("./images/bg.png")
    hero=HeroPlane("./images/hero1.png",screen,(400-100)/2,376)# 创建对象hero
    enemy2=EnemyPlane2(screen)
    while True:
        screen.blit(background,(0,0))
        show_scroe=font.render("fengshu: %s " % (str(hero.score)),True,(250,250,0))
        move_step=10
        screen.blit(show_scroe,(0,0))

        hero.display()#调用方法

        clock=pygame.time.Clock()

        move(move_step,hero,enemy2)
        hero.shifoubao=False
        enemy2.dispp(hero)
        hero.panzha()

        pygame.display.update()
        clock.tick(60)

if __name__=="__main__":

    main()
