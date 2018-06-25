import pygame
def main():
    #创建游戏窗口
    chuangkou = pygame.display.set_mode((400,500),0,32)
    #把本地的文件夹的图片，获取到代码中
    beijing = pygame.image.load('./images/background.png')
    #bei = pygame.image.load('./images/enemy1.png')
    bbgg = pygame.image.load('./images/hero1.png')
    #定义好飞机的位置和大小
    weizhi = pygame.Rect((400-100)/2,350,100,124)
    clock = pygame.time.Clock()#pygame自带的时间控制器
    while True:
        #把图片加载到游戏窗口上
        chuangkou.blit(beijing,(0,0))
        chuangkou.blit(bbgg,weizhi)
        #移动位置
        weizhi.x=weizhi.x+1
        if weizhi.x > 400:#判断如果出了屏幕，就让他回到原来位置。
            weizhi.x = 0
        pygame.display.update()#更新游戏显示
        clock.tick(60)#每隔60分之一秒移动一下
if __name__=='__main__':
    main()
