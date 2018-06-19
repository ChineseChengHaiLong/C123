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
    def weizhi(self):#定义把飞机图加载到窗口上并定义位置
        self.chuangkou.blit(self.Feiphoto,self.Feiweizhi)
def feiji():#创建函数
    chuangkou = pygame.display.set_mode((600,700),0,32)#定义游戏窗口大小
    beijing = pygame.image.load('./images/background.png')#把背景图获取代码中
    hero = Feiji('./images/hero1.png',chuangkou)#创建一个飞机对象，传入路径参数
    clock = pygame.time.Clock()#pygame中自带的时间包
    move = 10#定义步长
    while True: #循环输出
        chuangkou.blit(beijing,(0,0))#打背景图获取到代码上
        hero.weizhi()#对象调用类属性，把飞机图获取到代码上并定义位置
        for i in pygame.event.get():#游戏事件的监听，控制
            if i.type == pygame.QUIT:#如果某一操作等于退出
                print('退出程序')
                pygame.quit()#退出程序
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            hero.Feiweizhi.x += move
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            hero.Feiweizhi.x -= move
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            hero.Feiweizhi.y -= move
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            hero.Feiweizhi.y += move
        pygame.display.update()#刷新显示
        clock.tick(60)#每隔多少秒运行一下
if __name__ == '__main__':#有权限的访问，只有自己可以调式，其他人调用不显示
    feiji()
