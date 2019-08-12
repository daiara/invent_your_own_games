import pygame, sys
from pygame.locals import *

pygame.init()

window_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render("Hello world!", True, white, blue)
text_rect = text.get_rect()
text_rect.centerx = window_surface.get_rect().centerx
text_rect.centery = window_surface.get_rect().centery

window_surface.fill(white)
pygame.draw.polygon(window_surface, green, ((146,0),(291,106),(236,277),(56,277),(0,106)))

pygame.draw.line(window_surface, blue, (60,60),(120,60),4)
pygame.draw.line(window_surface, blue, (120,60),(60,120))
pygame.draw.line(window_surface, blue, (60,120),(120,120),4)

pygame.draw.circle(window_surface, blue, (300,50), 20, 0)

pygame.draw.ellipse(window_surface, red, (300,250,40,80),1)

pygame.draw.rect(window_surface, red, (text_rect.left - 20, text_rect.top - 20, text_rect.width + 40, text_rect.height + 40))

pix_array = pygame.PixelArray(window_surface)
pix_array[480][380] = black
del pix_array

window_surface.blit(text, text_rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

