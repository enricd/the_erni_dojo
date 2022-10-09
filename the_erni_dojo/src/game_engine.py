"""
Game Engine for "The ERNI Dojo" core system

Author: Enric Domingo (enricd) @ERNI

--- Game engine should be agnostic to the specific Game, Rules and Agents ---
(high level idea:)

import game as Board
import agents

# init game
board = Board()

# game turns while loop
obs = board.curr_state
action = agent(obs)
board.next_turn(action)

----------------------------------------------------------------------------
"""

import pygame

from snake_2p import Snake2PGame as Board               # Game
from agents.clock_turns3_agent import agent as agent1   # Player 1
from agents.clock_turns3_agent import agent as agent2   # Player 2


def game_engine(play_id=0000):

    # --- Init board game ---
    board = Board(play_id)
    config = board.config

    # --- Game turns loop ---
    game_over = False
    turn = 0

    while not game_over and turn < config["max_turns"]:

        agent1_action = agent1(board.get_current_obs(agent_id=1), config)
        agent2_action = agent2(board.get_current_obs(agent_id=2), config)

        game_over, score_1, score_2, turn = board.play_step(agent1_action, agent2_action)

    print("Final Score", score_1, score_2)

    pygame.quit()


if __name__ == "__main__":
    game_engine()