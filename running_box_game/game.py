# Created by
# Pineda, Carl Dennis
# Ave, Shalom Jamaica
# Descalzo, Kayla Claudine
# CEIT - 37 - 501A

import pygame
import random

pygame.init()

# game constant variables
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
WIDTH = 450
HEIGHT = 300

# game variables
score = 0
active = False
player_x = 50
player_y = 200
y_change = 0
x_change = 0
gravity = 1
obstacles = [300, 450, 600]
obstacle_speed = 2
hi_score = 0

# program init
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Running Box")
background = black;
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
small = pygame.font.Font('freesansbold.ttf', 11)
big = pygame.font.Font('freesansbold.ttf', 26)
timer = pygame.time.Clock()

# run while the app is running
running = True
while running:
    # start the process
    timer.tick(fps)
    screen.fill(background)
    
    # Main Menu UI
    if not active:
        credit = small.render('Created by Pineda, Ave, and Descalzo', True, green, black)
        screen.blit(credit, (0,0))
        instruction_text = font.render(f'Press Space Bar to Start.', True, white, black)
        screen.blit(instruction_text, (140, 50))
        instruction_text2 = font.render(f'Space Bar = Jump. A/D to move', True, white, black)
        screen.blit(instruction_text2, (80, 90))
        title = big.render('Running Box', True, orange, black)
        screen.blit(title, (140, 120))
        highscore_text = font.render(f'High Score : {hi_score}', True, white, black)
        screen.blit(highscore_text, (160, 250))
    # Gameplay
    if active:
        score_text = font.render(f'Score : {score}', True, white, black)
        screen.blit(score_text, (160, 250))
    
    # Asset loading
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, blue, [player_x, player_y, 20, 20 ])
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0], 200, 20, 20])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, yellow, [obstacles[2], 200, 20, 20])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Reset when game over an press space
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [300, 450, 600]
                player_x = 50
                score = 0
                active = True
                obstacle_speed = 2
                
        # Activate when game is running
        # Holding down the key
        if event.type == pygame.KEYDOWN and active:
            # Jump
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
            # Move Right
            if event.key == pygame.K_d:
                x_change = 2
            # Move Left
            if event.key ==pygame.K_a:
                x_change = -2
        # Released the key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                x_change = 0
            if event.key == pygame.K_a:
                x_change = 0
    
    # Obstacle generation
    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(470, 570)
                score += 1
                obstacle_speed += 0.01
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                if score > hi_score:
                    hi_score = score
                active = False
                
    # Bound Checking Codes
    if 0 <= player_x <= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 430:
        player_x = 430
        
                
    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0
          
    pygame.display.flip()
pygame.quit()