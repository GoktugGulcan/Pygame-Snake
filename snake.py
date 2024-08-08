import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()
snake_block = 20
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list, direction):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    # Yılanın başı
    head = snake_list[-1]
    if direction == 'RIGHT':
        pygame.draw.circle(dis, white, (head[0] + 15, head[1] + 5), 3)
        pygame.draw.circle(dis, white, (head[0] + 15, head[1] + 15), 3)
    elif direction == 'LEFT':
        pygame.draw.circle(dis, white, (head[0] + 5, head[1] + 5), 3)
        pygame.draw.circle(dis, white, (head[0] + 5, head[1] + 15), 3)
    elif direction == 'UP':
        pygame.draw.circle(dis, white, (head[0] + 5, head[1] + 5), 3)
        pygame.draw.circle(dis, white, (head[0] + 15, head[1] + 5), 3)
    elif direction == 'DOWN':
        pygame.draw.circle(dis, white, (head[0] + 5, head[1] + 15), 3)
        pygame.draw.circle(dis, white, (head[0] + 15, head[1] + 15), 3)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = snake_block  
    y1_change = 0

    snake_List = []
    Length_of_snake = 3

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    direction = 'RIGHT'
    score = 0
    change_to = direction

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lose! C-Retry Q-Quit", red)
            your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'

        if change_to == 'LEFT':
            x1_change = -snake_block
            y1_change = 0
        elif change_to == 'RIGHT':
            x1_change = snake_block
            y1_change = 0
        elif change_to == 'UP':
            y1_change = -snake_block
            x1_change = 0
        elif change_to == 'DOWN':
            y1_change = snake_block
            x1_change = 0

        direction = change_to

        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width - snake_block
        if y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height - snake_block

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List, direction)
        your_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
