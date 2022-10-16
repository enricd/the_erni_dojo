def agent(obs, config):

    turn = obs["turn"]
    actions = config["actions"]

    if turn % 12 in [0, 1, 2]:
        return actions.UP

    elif turn % 12 in [3, 4, 5]:
        return actions.RIGHT

    elif turn % 12 in [6, 7, 8]:
        return actions.DOWN
        
    elif turn % 12 in [9, 10, 11]:
        return actions.LEFT

    else:
        return actions.UP