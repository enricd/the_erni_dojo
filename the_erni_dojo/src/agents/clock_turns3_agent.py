def agent(obs, config):

    turn = obs["turn"]
    action = config["actions"]

    if turn % 12 in [0, 1, 2]:
        return action.UP
    elif turn % 12 in [3, 4, 5]:
        return action.RIGHT
    elif turn % 12 in [6, 7, 8]:
        return action.DOWN
    elif turn % 12 in [9, 10, 11]:
        return action.LEFT

    else:
        return action.UP