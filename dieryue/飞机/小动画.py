import pygame
def donghua():
    clock = pygame.time.Clock()
    chuangkou = pygame.display.set_mode((500,500),0,32)
    L=['a','b','c','d','e','f','g','h','k','l','m','n','o','p','q','r','s','t','u']
    while True:
        for i in L:
            lu = './imagess/%s.jpg' % i
            beijing = pygame.image.load(lu)
            chuangkou.blit(beijing,(0,0))
            clock.tick(2)
            pygame.display.update()
    #while True:
     #   pass
        #pygame.display.update()
donghua()
