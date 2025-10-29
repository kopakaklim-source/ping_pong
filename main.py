from pygame import *
import sys
import pygame
init()
main_win = display.set_mode((700, 500))
display.set_caption('ping_pong')
background = transform.scale(image.load('assets/table.png'), (700, 500))

game = True
clock = time.Clock()
FPS = 60

while True:
    clock.tick(FPS)
    for event in pygame.event.get(): #событие
        if event.type == QUIT:
            quit()
            sys.exit()
    main_win.blit(background, (0, 0))    #первая отрисовка
    display.update()


