from random import randint
from pygame import *
import sys
import pygame
init()
main_win = display.set_mode((800, 500))
display.set_caption('ping_pong')
background = transform.scale(image.load('assets/table.png'), (800, 500))
main_win.fill((255, 255, 255))

game = True
clock = time.Clock()
FPS = 60 #это фпс

speed_x = randint(4, 6)
speed_y = 1.5

flag = True
flag1 = True

h = 0
g = 0
z = 0

font.init()
f1 = font.SysFont('Aharoni', 50)
f2 = font.SysFont('Aharoni', 50)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, image_height, image_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (image_height, image_width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))


class RacketLeft(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += 5
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        self.reset()

class RacketRight(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += 5
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        self.reset()

class Ball(GameSprite):
    def update(self):
        self.reset()

racket1 = RacketLeft('assets/racket1.png', 20, 200, 5, 75, 150)
racket2 = RacketRight('assets/racket2.png', 720, 200, 5, 75, 150)
ball1 = Ball('assets/ball.png', 400, 250, z, 70, 70)


while True:
    flag1 = True
    clock.tick(FPS)
    for event in pygame.event.get(): #событие
        if event.type == QUIT:
            quit()
            sys.exit()
    pygame.draw.rect(main_win, (255, 255, 255), racket1.rect, 0)
    pygame.draw.rect(main_win, (255, 255, 255), racket2.rect, 0)
    pygame.draw.rect(main_win, (255, 255, 255), ball1.rect, 0)
    main_win.blit(background, (0, 0))    #первая отрисовка
    ball1.rect.x += speed_x
    ball1.rect.y += speed_y
    racket1.update()
    racket2.update()
    ball1.update()
    if ball1.rect.y > 390 or ball1.rect.y < 70:
        if flag:
            speed_y *= -1
            flag = False
    if sprite.collide_rect(ball1, racket1) or sprite.collide_rect(ball1, racket2):
        if flag1:
            speed_x += 1
            speed_x *= -1
            flag1 = False
        flag = True
    if ball1.rect.x > 870:
        ball1.rect.x = 400
        ball1.rect.y = 250
        h += 1
        print('Счет левой ракетки: ', h)

    if ball1.rect.x < -70:
        ball1.rect.x = 400
        ball1.rect.y = 250
        g += 1
        print('Счет правой ракетки: ', g)
    display.update()



