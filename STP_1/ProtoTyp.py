import pygame
import math
import random

pygame.init()
pygame.mixer.init()

#variables

font=pygame.font.Font('press-start-2p 2/PressStart2P-Regular.ttf',12)
clock = pygame.time.Clock()
FPS = 30
SCREEN_WIDTH = 500
SCREEN_HEIGHT= 650

#game window

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless_Faller")

#load image
bg = pygame.image.load("FALLing.glitterBACKGROUND.jpg").convert()
bg_height = bg.get_height()
#define game variables
scroll = 0
tiles = math.ceil(SCREEN_HEIGHT/bg_height)+1

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (0,i*bg_height + scroll))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs(scroll) > (bg_height):
         scroll = 0
         
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
    pygame.display.update()
pygame.quit()

#loading image




