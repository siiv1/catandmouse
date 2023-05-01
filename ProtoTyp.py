import pygame
import math
import random
import os

pygame.init()
pygame.mixer.init()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#variables

font=pygame.font.Font('press-start-2p 2/PressStart2P-Regular.ttf',12)
clock = pygame.time.Clock()
FPS = 30
SCREEN_WIDTH = 500
SCREEN_HEIGHT= 650

#game window

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("__FVLL__")

#LOAD BCKGRND IMAGE
bg = pygame.image.load("FALLing.glitterBACKGROUND.png").convert()
bg_height = bg.get_height()
#define game variables
scroll = 0
tiles = math.ceil(SCREEN_HEIGHT/bg_height)+1


#Creating platform locations and generating the images
blocks = [[25, 100, 1], [25, 350, 1], [100, 600, 3], [300, 250, 3], [320, 500, 1]]
block_images =[]
for i in range (1, 4):
     img = pygame.image.load(f'viZuals/platformz/Platformz-{i}.png')
     block_images.append(img)

#player variables
player_x = 300
player_y = 20
Splayer =pygame.transform.scale(pygame.image.load("viZuals/SPlayer1.png"), (125,125))
direction = -1
y_speed = 0
gravity = 0.4
x_speed = 3
x_direction = 0
#Function that draws the platforms onto the screen, takes a list
#of images and their coordinates on screen and returns a list of platforms
def draw_platforms(block_list, platform_images):
    platforms = []
    for j in range(len(block_list)):
        image = platform_images[block_list[j][2]-1]
        platform = pygame.rect.Rect((block_list[j][0]+30, block_list[j][1]), (130, 10))
        if j==3 or j==2:
            screen.blit(image, (block_list[j][0]-100, block_list[j][1]))
            #pygame.draw.rect(screen, 'papaya whip', platform)
            platforms.append(platform)
        else:
            screen.blit(image, (block_list[j][0], block_list[j][1]))
            #pygame.draw.rect(screen, 'papaya whip', platform)
            platforms.append(platform)

    return platforms

def draw_player(x_pos, y_pos, player_img, direction):
     screen.blit(player_img, (x_pos, y_pos))
     player_rect = pygame.rect.Rect((x_pos+62, y_pos+25), (30, 90))
     pygame.draw.rect(screen, 'white', player_rect, 2)
     return player_rect


#GAME LOOP
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
         
#platforms
    block_platforms = draw_platforms(blocks, block_images)
#player
    player = draw_player(player_x, player_y, Splayer, direction)
    for i in range(len(block_platforms)):
        if direction == -1 and player.colliderect(block_platforms[i]):
            y_speed += -1
            if y_speed > -7:
                y_speed = -7
#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_direction = -1
            elif event.key == pygame.K_RIGHT:
                x_direction = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_direction = 0
            elif event.key == pygame.K_RIGHT:
                x_direction = 0

    y_speed += gravity
    player_y += y_speed+2
    if y_speed < 0:
        direction = 1
    else: 
         direction = -1

    player_x += x_speed*x_direction
    
    pygame.display.update()
pygame.quit()
