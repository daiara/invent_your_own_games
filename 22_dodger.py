import pygame, sys, random
from pygame.locals import *

window_width = 600
window_height = 600
text_color = (0,0,0)
background_color = (255,255,255)
fps = 60
baddie_min_size = 10
baddie_max_size = 40
baddie_min_speed = 1
baddie_max_speed = 8
add_new_baddie_rate = 6
player_move_rate = 5

def terminate():
    pygame.quit()
    sys.exit()

def wait_for_player():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def player_has_hit_baddie(player_rect, baddies):
    for b in baddies:
        if player_rect.colliderect(b['rect']):
            return True
    return False

def draw_text(text, font, surface, x, y):
    text_obj = font.render(text, 1, text_color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(text_obj,text_rect)

pygame.init()
main_clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 48)

game_over_sound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

player_image = pygame.image.load('player.png')
player_rect = player_image.get_rect()
baddie_image = pygame.image.load('baddie.png')

window_surface.fill(background_color)
draw_text('Dodger', font, window_surface, (window_width/3),(window_height/3))
draw_text('Press a key to start', font, window_surface, (window_width/3) - 30, (window_height/3) + 50)
pygame.display.update()
wait_for_player()

top_score = 0
while True:
    baddies = []
    score = 0
    player_rect.topleft = (window_width/2,window_height - 50)
    move_left = move_right = move_up = move_down = False
    reverse_cheat = slow_cheat = False
    baddie_add_counter = 0
    pygame.mixer.music.play(-1,0.0)

    while True:
        score += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        
            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverse_cheat = True
                if event.key == K_x:
                    slow_cheat = True
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
                if event.key == K_z:
                    reverse_cheat = False
                    score = 0
                if event.key == K_x:
                    slow_cheat = False
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    move_left = False
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = False
                if event.key == K_UP or event.key == K_w:
                    move_up = False
                if event.key == K_DOWN or event.key == K_s:
                    move_down = False
                
            if event.type == MOUSEMOTION:
                player_rect.centerx = event.pos[0]
                player_rect.centery = event.pos[1]
            
        if not reverse_cheat and not slow_cheat:
            baddie_add_counter += 1
        if baddie_add_counter == add_new_baddie_rate:
            baddie_add_counter = 0
            baddie_size = random.randint(baddie_min_size,baddie_max_size)
            new_baddie = {'rect': pygame.Rect(random.randint(0, window_width - baddie_size), 0 - baddie_size, baddie_size, baddie_size), 
            'speed': random.randint(baddie_min_speed, baddie_max_size),
            'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size)),
            }
            baddies.append(new_baddie)
        
        if move_left and player_rect.left > 0:
            player_rect.move_ip(-1 * player_move_rate, 0)
        if move_right and player_rect.right < window_width:
            player_rect.move_ip(player_move_rate, 0)
        if move_up and player_rect.top > 0:
            player_rect.move_ip(0, -1 * player_move_rate)
        if move_down and player_rect.bottom < window_height:
            player_rect.move_ip(0, player_move_rate)

        for b in baddies:
            if not reverse_cheat and not slow_cheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverse_cheat:
                b['rect'].move_ip(0, -5)
            elif slow_cheat:
                b['rect'].move_ip(0,1)

        for b in baddies[:]:
            if b['rect'].top > window_height:
                baddies.remove(b)

        window_surface.fill(background_color)

        draw_text('Score: %s' % (score), font, window_surface, 10, 0)
        draw_text('Top score: %s' % (top_score), font, window_surface, 10, 40)

        window_surface.blit(player_image, player_rect)

        for b in baddies:
            window_surface.blit(b['surface'],b['rect'])

        pygame.display.update()

        if player_has_hit_baddie(player_rect, baddies):
            if score > top_score:
                top_score = score
            break
        
        main_clock.tick(fps)
    
    pygame.mixer.music.stop()
    game_over_sound.play()

    draw_text('Game over', font, window_surface, (window_width/3), (window_height/3))
    draw_text('Press a key to play again.', font, window_surface, (window_width/3) - 80, (window_height/3) + 50)
    pygame.display.update()
    wait_for_player()

    game_over_sound.stop()