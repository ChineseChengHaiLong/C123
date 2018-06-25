import pygame
import time
class Photo(object):
    def __init__(self,lujing,chuangkou):
        self.x = 0
        self.y = 0
        self.w = 800
        self.h = 500
        self.chuangkou=chuangkou
        self.lujing=lujing
        self.tupian = pygame.image.load(self.lujing)
        self.weizhi = pygame.Rect(self.x,self.y,self.w,self.h)
    def chuangjian(self):
        self.chuangkou.blit(self.tupian,self.weizhi)
def donghua():
    clock = pygame.time.Clock()
    chuangkou = pygame.display.set_mode((266,157),0,32)
    L=['a','b','c','d','e','f','g','h','k','l','m','n','o','p','q','r','s','t','u']
    while True:
        time.sleep(1)
        for i in L:
            lu = './imagess/%s.jpg' % i
           # beijing = pygame.image.load(lu)
            #chuangkou.blit(beijing,(0,0))
            hero = Photo(lu,chuangkou)
            hero.chuangjian()
            clock.tick(10)
            pygame.display.update()
    while True:
        pass
        #pygame.display.update()
donghua()
