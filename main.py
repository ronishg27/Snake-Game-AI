import pygame
import random
from model import ai_action
pygame.init()

# Game settings
width, height = 640, 480
cell_size = 20

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake settings
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'
change_to = direction

# Food settings
food_pos = [random.randrange(1, width//cell_size) * cell_size, random.randrange(1, height//cell_size) * cell_size]
food_spawn = True

# game state
def get_game_state():
    return {
        "snake": snake,
        "food": food_pos,
        "direction": direction
    }

actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']




# Game over
def game_over():
    pygame.quit()
    quit()

# Main loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()

        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    game_state = get_game_state()
    direction = ai_action(game_state, direction)
 
    
    # Move snake
    if direction == 'UP':
        snake[0] = (snake[0][0], snake[0][1] - cell_size)
    if direction == 'DOWN':
        snake[0] = (snake[0][0], snake[0][1] + cell_size)
    if direction == 'LEFT':
        snake[0] = (snake[0][0] - cell_size, snake[0][1])
    if direction == 'RIGHT':
        snake[0] = (snake[0][0] + cell_size, snake[0][1])
    
    # Snake body growing mechanism
    snake.insert(0, list(snake[0]))
    if snake[0] == food_pos:
        food_spawn = False
    else:
        snake.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, width//cell_size) * cell_size, random.randrange(1, height//cell_size) * cell_size]
    food_spawn = True
    
    screen.fill(black)
    
    for pos in snake:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
    
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))
    
    # Game Over conditions
    if snake[0][0] < 0 or snake[0][0] > width-cell_size:
        game_over()
    if snake[0][1] < 0 or snake[0][1] > height-cell_size:
        game_over()
    for block in snake[1:]:
        if snake[0] == block:
            game_over()
    
    pygame.display.flip()
    clock.tick(10)
