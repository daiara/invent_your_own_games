import pygame, sys, random
from pygame.locals import *

pygame.init()
main_clock = pygame.time.Clock()

window_width = 400
window_height = 400
window_sufarce = pygame.display.set_mode((window_width,window_height), 0, 32)
pygame.display.set_caption('Collision Detection')

black = (0,0,0)
green = (0,255,0)
white = (255,255,255)

food_counter = 0
new_food = 40
food_size = 20
player = pygame.Rect(300,100,50,50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, window_width - food_size), random.randint(0, window_height - food_size), food_size, food_size))

move_left = False
move_right = False
move_up = False
move_down = False

move_speed = 6

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if event.type == KEYDOWN:
        if event.key == K_LEFT or event.key == K_a:
            move_right = False
            move_left = True
        if event.key == K_RIGHT or event.key  == K_d:
            move_left = False
            move_right = True
        if event.key == K_UP or event.key  == K_w:
            move_down = False
            move_up = True
        if event.key == K_DOWN or event.key == K_s:
            move_down = True
            move_up = False
    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.key == K_LEFT or event.key == K_a:
            move_left = False
        if event.key == K_RIGHT or event.key == K_d:
            move_right = False
        if event.key == K_UP or event.key == K_w:
            move_up = False
        if event.key == K_DOWN or event.key == K_s:
            move_down = False
        if event.key == K_x:
            player.top = random.randint(0, window_height - player.height)
            player.left = random.randint(0, window_width - player.width)
    
    if event.type == MOUSEBUTTONUP:
        foods.append(pygame.Rect(event.pos[0], event.pos[1], food_size, food_size))

    food_counter += 1
    if food_counter >= new_food:
        foods.append(pygame.Rect(random.randint(0, window_width - food_size), random.randint(0, window_height - food_size), food_size, food_size))

    window_sufarce.fill(white)

    if move_down and player.bottom < window_height:
        player.top += move_speed
    if move_up and player.top > 0:
        player.top -= move_speed
    if move_left and player.left > 0:
        player.left -= move_speed
    if move_right and player.right < window_width:
        player.right += move_speed

    pygame.draw.rect(window_sufarce, black, player)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    for i in range(len(foods)):
        pygame.draw.rect(window_sufarce, green, foods[i])

    pygame.display.update()
    main_clock.tick(40)    