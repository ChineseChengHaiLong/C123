import pygame
def aa():
    b = pygame.display.set_mode((265,154),0,32)
    a = pygame.image.load('./imagess/a.jpg')
    b.blit(a,(0,0))
    pygame.display.update()
    while True:
        pass
aa()
