import pygame, sys, time
from pygame.locals import *

pygame.init()

window_width = 400
window_height = 400
window_surface = pygame.display.set_mode((window_width,window_height), 0, 32)
pygame.display.set_caption('Animation')

down_left = 'downleft'
down_right = 'downright'
up_left = 'upleft'
up_right = 'upright'

move_speed = 4

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

b1 = {'rect':pygame.Rect(300,80,50,100),'color':red,'dir':up_right}
b2 = {'rect':pygame.Rect(200,200,20,20),'color':green,'dir':up_left}
b3 = {'rect':pygame.Rect(100,150,60,60),'color':blue,'dir':down_left}
boxes = [b1,b2,b3]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window_surface.fill(white)

    for b in boxes:
        if b['dir'] == down_left:
            b['rect'].left -= move_speed
            b['rect'].top += move_speed
        if b['dir'] == down_right:
            b['rect'].left += move_speed
            b['rect'].top += move_speed
        if b['dir'] == up_left:
            b['rect'].left -= move_speed
            b['rect'].top -= move_speed
        if b['dir'] == up_right:
            b['rect'].left += move_speed
            b['rect'].top -= move_speed

        if b['rect'].top < 0:
            if b['dir'] == up_left:
                b['dir'] = down_left
            if b['dir'] == up_right:
                b['dir'] = down_right
        if b['rect'].bottom > window_height:
            if b['dir'] == down_left:
                b['dir'] = up_left
            if b['dir'] == down_right:
                b['dir'] = up_right
        if b['rect'].left < 0:
            if b['dir'] == down_left:
                b['dir'] = down_right
            if b['dir'] == up_left:
                b['dir'] = up_right
        if b['rect'].right > window_width:
            if b['dir'] == down_right:
                b['dir'] = down_left
            if b['dir'] == up_right:
                b['dir'] = up_left

        pygame.draw.rect(window_surface, b['color'], b['rect'])
    pygame.display.update()
    time.sleep(0.02)