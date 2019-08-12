import pygame, sys, time, random
from pygame.locals import *

pygame.init()
main_clock = pygame.time.Clock()

window_width = 400
window_height = 400
window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('Sprits and Sounds')

white = (255,255,255)

player = pygame.Rect(300, 100, 40, 40)
player_image = pygame.image.load('donald.png')
player_stretched_image = pygame.transform.scale(player_image, (40, 40))
food_image = pygame.image.load('cake.png')
food_stretched_image = pygame.transform.scale(food_image, (30, 30))

foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, window_width - 20), random.randint(0, window_height - 20), 20, 20))

food_counter = 0
new_food = 40

move_left = False
move_right = False
move_up = False
move_down = False

move_speed = 6

pick_up_sound = pygame.mixer.Sound('gulp.wav')
pygame.mixer.music.load('super.wav')
pygame.mixer.music.play(-1, 0.0)
music_playing = True


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
        if event.key == K_m:
            if music_playing:
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play(-1, 0.0)
            music_playing = not music_playing
    if event.type == MOUSEBUTTONUP:
        foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))
    
    food_counter += 1
    if food_counter >= new_food:
        food_counter = 0
        foods.append(pygame.Rect(random.randint(0, window_width - 20), random.randint(0, window_height - 20), 20, 20))

    window_surface.fill(white)

    if move_down and player.bottom < window_height:
        player.top += move_speed
    if move_up and player.top > 0:
        player.top -= move_speed
    if move_left and player.left > 0:
        player.left -= move_speed
    if move_right and player.right < window_width:
        player.right += move_speed

    window_surface.blit(player_stretched_image, player)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            player_stretched_image = pygame.transform.scale(player_image, (player.width, player.height))
            if music_playing:
                pick_up_sound.play()
    
    for food in foods:
        window_surface.blit(food_stretched_image, food)

    pygame.display.update()
    main_clock.tick(40)