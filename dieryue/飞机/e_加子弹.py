import pygame  #导入pygame包
class Feiji(object):   #创建飞机类
    #初始值飞机图片路径、游戏窗口
    def __init__(self,ing_path,chuangkou):
        self.x=(400-100)/2
        self.y=350
        self.w=100
        self.h=124
        self.chuangkou=chuangkou#游戏窗口
        self.ing_path=ing_path#飞机路径
        self.Feiphoto = pygame.image.load(self.ing_path)#飞机图获取代码中，背景
        self.Feiweizhi = pygame.Rect(self.x,self.y,self.w,self.h)#飞机的位置
        self.bullet_list=[]# 定义子弹的保存列表
    def weizhi(self):#定义把飞机图加载到窗口上并定义位置
        self.chuangkou.blit(self.Feiphoto,self.Feiweizhi)
        for i in self.bullet_list:  #显示子弹
            i.weizhi()  #子弹的对像.weizhi()
            i.move()
     # 发射子弹
    def fire(self):
        a = Zidan('./images/bullet.png',self.chuangkou,self.Feiweizhi.x,self.Feiweizhi.y)#定义子弹的对象
        self.bullet_list.append(a)#把子弹追加到子弹列表中
class Zidan(object):   #创建子弹类
    #初始值子弹图片路径、游戏窗口
    def __init__(self,ing_path,chuangkou,x,y):
        self.x=x
        self.y=y
        self.chuangkou=chuangkou#游戏窗口
        self.ing_path=ing_path#子弹路径
        self.bulletphoto = pygame.image.load(self.ing_path)#子弹图获取代码中，背景
    def weizhi(self):#定义把子弹图加载到窗口上并定义位置
        self.chuangkou.blit(self.bulletphoto,(self.x,self.y))
    def move(self):
        self.y -= 2
def jianshi(hero,move):
        for i in pygame.event.get():#游戏事件的监听，控制
            if i.type == pygame.QUIT:#如果某一操作等于退出
                print('退出程序')
                pygame.quit()#退出程序
                exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    hero.fire()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]or keys[pygame.K_x]:
            hero.fire()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            hero.Feiweizhi.x += move
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            hero.Feiweizhi.x -= move
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            hero.Feiweizhi.y -= move
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            hero.Feiweizhi.y += move
def feiji():#创建函数
    chuangkou = pygame.display.set_mode((600,700),0,32)#定义游戏窗口大小
    beijing = pygame.image.load('./images/background.png')#把背景图获取代码中
    clock = pygame.time.Clock()#pygame中自带的时间包
    hero = Feiji('./images/hero1.png',chuangkou)#创建一个飞机对象，传入路径参数
    
    while True: #循环输出
        jianshi(hero,10)
        chuangkou.blit(beijing,(0,0))#打背景图获取到代码上
        hero.weizhi()#对象调用类属性，把飞机图获取到代码上并定义位置
        pygame.display.update()#刷新显示
        clock.tick(60)#每隔多少秒运行一下
if __name__ == '__main__':#有权限的访问，只有自己可以调式，其他人调用不显示
    feiji()
