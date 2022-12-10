# Created by
# Pineda, Carl Dennis
# Ave, Shalom Jamaica
# Descalzo, Kayla Claudine
# CEIT - 37 - 501A
# Passed to Professor Reynaldo Alvez of Game Analysis

import random
import pygame

pygame.init()

# game constant variables
WIDTH = 900
HEIGHT = 500
fps = 60

# color palette
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)
yellow = (255, 255, 0)

# music
pygame.mixer.init()
pygame.mixer.music.load('./bird_in_the_space_game/bgm.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# window setting
pygame.display.set_caption('Bird in the Space')
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
small = pygame.font.Font('freesansbold.ttf', 11)
big = pygame.font.Font('freesansbold.ttf', 26)

# Game Variables
score = 0
hi_score = 0
player_x = 225
player_y = 225
y_change = 0
jump_height = 12
gravity = .9
obstacles = [400, 700, 1000, 1300, 1600]
obstacle_speed = 3
star_speed = .5
generate_places = True
y_positions = []
active = False
stars = []

def draw_player(x_pos, y_pos):
    global y_change
    mouth = pygame.draw.circle(screen, gray, (x_pos + 25, y_pos + 15), 12)
    play = pygame.draw.rect(screen, white, [x_pos, y_pos, 30, 30], 0, 12)
    eye = pygame.draw.circle(screen, black, (x_pos + 24, y_pos + 12), 5)
    jetpack = pygame.draw.rect(screen, white, [x_pos - 20, y_pos, 18, 28], 3, 2)
    # draw flames when jumping
    if y_change < 0:
        flame1 = pygame.draw.rect(screen, red, [x_pos - 20, y_pos + 29, 7, 20], 0, 2)
        flame1_yellow = pygame.draw.rect(screen, yellow, [x_pos - 18, y_pos +30, 3, 10], 0, 2)
        flame2 = pygame.draw.rect(screen, red, [x_pos - 10, y_pos + 29, 7, 20], 0, 2)
        flame2_yellow = pygame.draw.rect(screen, yellow, [x_pos - 8, y_pos +30, 3, 10], 0, 2)
    return play

def draw_obstacles(obst, y_pos, play):
    global active
    for i in range(len(obst)):
        obstacle_height = y_pos[i]
        # obstacle spawn
        top_rect = pygame.draw.rect(screen, gray, [obst[i], 0, 30, obstacle_height])
        top_design = pygame.draw.rect(screen, gray, [obst[i] - 3, obstacle_height - 20, 36, 20], 0, 5)
        bot_rect = pygame.draw.rect(screen, gray, [obst[i], obstacle_height + 200, 30, HEIGHT - (obstacle_height - 70)])
        bot_design = pygame.draw.rect(screen, gray, [obst[i] - 3, obstacle_height + 200, 36, 20], 0, 5)
        if top_rect.colliderect(play) or bot_rect.colliderect(play):
            active = False

# background drawing
def draw_stars(stars):
    global total
    for i in range(total - 1):
        pygame.draw.rect(screen, white, [stars[i][0], stars[i][1], 3, 3], 0, 2)
        stars[i][0] -= star_speed
        if stars[i][0] < -3:
            stars [i][0] = WIDTH + 3
            stars[i][1] = random.randint(0, HEIGHT)
    return stars

running = True
while running:
    timer.tick(fps)
    screen.fill(black)
    
    if generate_places:
        for i in range(len(obstacles)):
            y_positions.append(random.randint(0, 300))
        total = 100
        for i in range(total):
            x_pos = random.randint(0, WIDTH)
            y_pos = random.randint(0, HEIGHT)
            stars.append([x_pos, y_pos])
        generate_places = False
    
    stars = draw_stars(stars)
    player = draw_player(player_x, player_y)
    draw_obstacles(obstacles, y_positions, player)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and active:
                y_change = -jump_height
            if event.key == pygame.K_RETURN and not active:
                player_y = 225
                player_x = 225
                y_change = 0
                generate_places = True
                obstacles = [400, 700, 1000, 1300, 1600]
                y_positions = []
                score = 0
                pygame.mixer.music.play()
                obstacle_speed = 3
                active = True
                
    # bound checking
    if player_y + y_change < HEIGHT - 30:
        player_y += y_change
        y_change += gravity
    else:
        player_y = HEIGHT - 30
        
    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < -30:
                obstacles.remove(obstacles[i])
                y_positions.remove(y_positions[i])
                obstacles.append(random.randint(obstacles[-1] + 280, obstacles[-1] + 320))
                y_positions.append(random.randint(0, 300))
                score += 1
                obstacle_speed += 0.1
    
    if active:
        score_text = font.render(f'Score : {score}', True, white)
        screen.blit(score_text, (10, 450))
    
    if not active:
        credit = small.render('Created by Pineda, Ave, and Descalzo', True, green)
        screen.blit(credit,(0,0))
        
        title_text = big.render('Rocket Bird', True, blue)
        screen.blit(title_text, (380, 200))
        
        instruction_text = font.render('Press Space Bar to Jump, avoid obstacles', True, white)
        screen.blit(instruction_text, (250, 300))
        
        instruction_text2 = font.render('Press Enter to Start', True, white)
        screen.blit(instruction_text2, (320, 350))
        if score > hi_score:
            hi_score = score
            
        hi_score_text = font.render(f'Highscore : {hi_score}', True, white)
        screen.blit(hi_score_text, (10, 470))
            
    pygame.display.flip()
pygame.quit()