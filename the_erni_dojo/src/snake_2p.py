import pygame
import random
from enum import Enum
from collections import namedtuple
import os
from pathlib import Path

from agents import clock_turns3_agent as agent

pygame.init()
font = pygame.font.SysFont("Ariel", 25)

# reset
# reward 
# play(action) -> direction
# game_iteration
# is_collision


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple("Point", "x, y")

# rgb colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
GREEN1 = (0, 150, 0)
GREEN2 = (0, 255, 0)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 10


class Snake2PGame:

    def __init__(self, play_id, w=720, h=720):
        self.play_id = play_id
        self.game_plays_folder = Path(f"../game_plays/play_{self.play_id:0>4d}")
        if not os.path.exists(self.game_plays_folder):
            os.mkdir(self.game_plays_folder)

        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        # init game state
        self.direction_1 = Direction.RIGHT
        self.direction_2 = Direction.RIGHT

        self.head_1 = Point(self.w//2 + (5*BLOCK_SIZE), self.h//2 + (5*BLOCK_SIZE))
        self.snake_1 = [self.head_1,
                      Point(self.head_1.x - BLOCK_SIZE, self.head_1.y),
                      Point(self.head_1.x - (2*BLOCK_SIZE), self.head_1.y)]

        self.head_2 = Point(self.w//2 - (5*BLOCK_SIZE), self.h//2 - (5*BLOCK_SIZE))
        self.snake_2 = [self.head_2,
                      Point(self.head_2.x-BLOCK_SIZE, self.head_2.y),
                      Point(self.head_2.x-(2*BLOCK_SIZE), self.head_2.y)]

        self.score_1 = 0
        self.score_2 = 0
        self.food = None
        self._place_food()

        self.config = {
            "actions": Direction,
            "max_turns": 50
            }

        self.turn = 0


    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE ) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE ) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in (self.snake_1 + self.snake_2):
            self._place_food()


    def play_step(self, agent_1_action, agent_2_action):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # self.direction = Direction.LEFT
        # self.direction = Direction.RIGHT
        # self.direction = Direction.UP
        # self.direction = Direction.DOWN

        self.direction_1 = agent_1_action
        self.direction_2 = agent_2_action

        # 2. Move
        self.head_1 = self._move(self.head_1, self.direction_1)  # update the head
        self.head_2 = self._move(self.head_2, self.direction_2)

        self.snake_1.insert(0, self.head_1)
        self.snake_2.insert(0, self.head_2)

        # 3. Check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score_1, self.score_2, self.turn-1

        # 4. Place new food or just move
        if self.head_1 == self.food:
            self.score_1 += 1
            self._place_food()
        else:
            self.snake_1.pop()

        if self.head_2 == self.food:
            self.score_2 += 1
            self._place_food()
        else:
            self.snake_2.pop()

        # 5. Update UI, clock, and save display image
        self._update_ui()
        pygame.image.save(self.display, (self.game_plays_folder / f"turn_{self.turn:0>4d}.jpg"))
        self.clock.tick(SPEED)
        self.turn += 1

        # 6. Return game over, scores and turn number
        return game_over, self.score_1, self.score_2, self.turn-1


    def _is_collision(self):
        # Hits boundary
        if self.head_1.x > self.w - BLOCK_SIZE or \
            self.head_1.x < 0 or \
            self.head_1.y > self.h - BLOCK_SIZE or \
            self.head_1.y < 0:
            print("1 boundary collision", self.head_1)
            return True
        
        if self.head_2.x > self.w - BLOCK_SIZE or \
            self.head_2.x < 0 or \
            self.head_2.y > self.h - BLOCK_SIZE or \
            self.head_2.y < 0:
            print("2 boundary collision", self.head_2)
            return True

        # Hits itself
        if self.head_1 in (self.snake_1[1:] + self.snake_2):
            print("hits 1")
            return True

        if self.head_2 in (self.snake_2[1:] + self.snake_1):
            print("hits 2")
            return True

        return False 


    def _update_ui(self):
        self.display.fill(BLACK)    

        for pt in self.snake_1:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, BLOCK_SIZE-4, BLOCK_SIZE-4))

        for pt in self.snake_2:
            pygame.draw.rect(self.display, GREEN1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, GREEN2, pygame.Rect(pt.x+4, pt.y+4, BLOCK_SIZE-4, BLOCK_SIZE-4))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text1 = font.render("Score 1: " + str(self.score_1), True, BLUE1)
        self.display.blit(text1, [0, 0])
        text_turn = font.render("Turn: " + str(self.turn), True, WHITE)
        self.display.blit(text_turn, [self.w//2-30, 0])
        text2 = font.render("Score 2: " + str(self.score_2), True, GREEN1)
        self.display.blit(text2, [self.w-90, 0])
        pygame.display.flip()


    def _move(self, head, direction):
        # update move of snake_1
        x = head.x
        y = head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE

        return Point(x, y)

    
    def get_current_obs(self, agent_id=None):
        turn = self.turn

        obs = {
            "agent_id": agent_id,
            "turn": turn,
            #snake_1
            #snake_2
            #food
        }

        return obs
        


if __name__ == "__main__":
    game = Snake2PGame()
    config = game.config

    # Game loop
    while True:

        agent1_action = agent(game.get_current_obs(agent_id=1), config)
        agent2_action = agent(game.get_current_obs(agent_id=2), config)

        game_over, score_1, score_2, turn = game.play_step(agent1_action, agent2_action)
        print(turn)

        if game_over == True:
            break
    
    print("Final Score", score_1, score_2)

    pygame.quit()
