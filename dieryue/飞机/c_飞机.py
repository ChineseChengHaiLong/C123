import pygame
'''
class Feiji(object):
    def __init__(self,ing_path,chuangkou):#初始化图片的路径，游戏窗口，定义战机的位置及大小，背景图片
        self.chuangkou=chuangkou#游戏窗口
        self.x=(400-100)/2
        self.y=350
        self.w=100
        self.h=124
        self.ing_path=ing_path#路径
        self.feiimage = pygame.image.load(self.ing_path)#把战机的图片获取到代
        self.weizhi = pygame.Rect(self.x,self.y,self.w,self.h)#战机的位置大小
    def display(self):
        self.chuangkou.blit((self.feiimage),self.weizhi)#把战机的图片及出现的位置加载到游戏窗口上
'''
def main():
    #创建游戏窗口
    chuangkou = pygame.display.set_mode((400,500),0,32)
    #把本地的文件夹的图片，获取到代码中
    beijing = pygame.image.load('./images/background.png')#大背景
    diji = pygame.image.load('./images/enemy1.png')#敌机
    bbgg = pygame.image.load('./images/hero1.png')#我方作战机
    #定义好飞机的位置和大小
    zuobiao = pygame.Rect(20,35,80,95)#敌机在做标
    weizhi = pygame.Rect((400-100)/2,350,100,124)#我方战机坐标
    clock = pygame.time.Clock()#pygame自带的时间控制器
    move = 10
    while True:
        #把图片加载到游戏窗口上
        chuangkou.blit(beijing,(0,0))#把大背景追加到游戏窗口上
        chuangkou.blit(diji,zuobiao)#把敌机图片追加到游戏窗口上
        chuangkou.blit(bbgg,weizhi)#把我方战机图片在追加到游戏窗口上
        #移动位置
  
        zuobiao.x=zuobiao.x+1
       # if weizhi.x > 400:#判断如果出了屏幕，就让他回到原来位置。
        #    weizhi.x = 0
        if zuobiao.x > 400:
            zuobiao.x = 0
        for event in pygame.event.get():#获取屏幕上的所有信息
            print('event.type=',event.type)
            print('event=',event)
            if event.type == pygame.QUIT:#当信息等于退出时
                print('退出游戏')
                pygame.quit()#退出程序
                exit()#退出程序
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    weizhi.y -= move
                elif event.key == pygame.K_DOWN:
                    weizhi.y += move
                elif event.key == pygame.K_LEFT:
                    weizhi.x -= move
                elif event.key == pygame.K_RIGHT:
                    weizhi.x += move
            elif event.type == pygame.KEYUP:
                pass
        pygame.display.update()#更新游戏显示
        clock.tick(60)#每隔60分之一秒移动一下
if __name__=='__main__':#内部调式，其他无权调用
    main()
