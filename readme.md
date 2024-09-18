
# Snake Game Documentation

## Overview
This project implements a simple Snake game using the `pygame` library, where the player controls a snake that moves around a grid, eating food and growing in size. The game ends if the snake runs into a wall or into itself. Additionally, the game features an AI that controls the snake’s movement toward the food.

## Files
- **main.py**: The main game loop that handles rendering, movement, and collision detection.
- **model.py**: Contains the AI logic that determines the snake’s movement direction based on the snake’s position and the location of the food.

---

## main.py

### Dependencies
```python
import pygame
import random
from model import ai_action
```
This script uses `pygame` to handle the game's graphical interface and `random` to randomly place food on the screen. The AI logic is imported from the `model.py` file.

### Game Settings
```python
width, height = 640, 480
cell_size = 20
```
The game screen is initialized to be 640x480 pixels, and the snake and food occupy grid cells of 20x20 pixels.

### Colors
```python
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
```
Basic color definitions for rendering game elements.

### Snake Settings
```python
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'
change_to = direction
```
The snake is initialized as a list of coordinates representing its body, starting with three segments.

### Food Settings
```python
food_pos = [random.randrange(1, width // cell_size) * cell_size, random.randrange(1, height // cell_size) * cell_size]
food_spawn = True
```
The food is placed randomly within the game grid and re-spawned once consumed by the snake.

### Game State
```python
def get_game_state():
    return {
        "snake": snake,
        "food": food_pos,
        "direction": direction
    }
```
This function returns the current game state, including the snake’s position, food position, and the current movement direction.

### Event Handling
```python
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
```
The game listens for keyboard events to allow the player to manually control the snake. The direction is updated based on the key pressed.

### Movement and AI
```python
game_state = get_game_state()
direction = ai_action(game_state, direction)
```
The AI logic from `model.py` is used to determine the snake's movement based on the game state.

### Snake Movement
```python
if direction == 'UP':
    snake[0] = (snake[0][0], snake[0][1] - cell_size)
elif direction == 'DOWN':
    snake[0] = (snake[0][0], snake[0][1] + cell_size)
elif direction == 'LEFT':
    snake[0] = (snake[0][0] - cell_size, snake[0][1])
elif direction == 'RIGHT':
    snake[0] = (snake[0][0] + cell_size, snake[0][1])
```
Moves the snake in the current direction by updating the coordinates of the snake's head.

### Food Consumption
```python
if snake[0] == food_pos:
    food_spawn = False
else:
    snake.pop()
```
If the snake’s head reaches the food position, the food is consumed, and the snake grows. Otherwise, the snake’s tail is removed to maintain its length.

### Collision Detection
```python
if snake[0][0] < 0 or snake[0][0] > width - cell_size:
    game_over()
if snake[0][1] < 0 or snake[0][1] > height - cell_size:
    game_over()
for block in snake[1:]:
    if snake[0] == block:
        game_over()
```
The game checks if the snake’s head has collided with the walls or with its own body, and ends the game if a collision occurs.

---

## model.py

### ai_action Function
```python
def ai_action(game_state, direction):
    snake = game_state['snake']
    food = game_state['food']
    
    if snake[0][0] < food[0]:
        if direction != 'RIGHT':
            return 'RIGHT'
    elif snake[0][0] > food[0]:
        if direction != 'LEFT':
            return 'LEFT'
    elif snake[0][1] < food[1]:
        if direction != 'DOWN':
            return 'DOWN'
    else:
        if direction != 'UP':
            return 'UP'
```
This function takes the current game state and the current direction as input and returns the direction that moves the snake closer to the food. The logic checks the relative position of the snake’s head and the food to determine whether to move `UP`, `DOWN`, `LEFT`, or `RIGHT`.

---

## Game Over Function
```python
def game_over():
    pygame.quit()
    quit()
```
This function terminates the game by closing the `pygame` window and quitting the program when a collision occurs.

---

## How to Run

1. Ensure that `pygame` is installed:
   ```bash
   pip install pygame
   ```

2. Run the game:
   ```bash
   python main.py
   ```


