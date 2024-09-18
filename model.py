def ai_action(game_state, direction):
    snake = game_state['snake']
    food = game_state['food']
    
    if snake[0][0] < food[0]:
      if(direction!='RIGHT'):
        print('RIGHT')
      return 'RIGHT'
    elif snake[0][0] > food[0]:
      if(direction!='LEFT'):
        print('LEFT')
      return 'LEFT'
    elif snake[0][1] < food[1]:
      if(direction!='DOWN'):
        print('DOWN')
      return 'DOWN'
    else:
      if(direction!='UP'):
        print('UP')
      return 'UP'
