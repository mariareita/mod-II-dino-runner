import random
import pygame
from dino_runner.components.obstacle.bird import Bird
from dino_runner.components.obstacle.cactus_small import SmallCactus
from dino_runner.components.obstacle.large_cactus import LargeCactus
from dino_runner.utils.constants import BIRD, DEFAULT_TYPE, LARGE_CACTUS, SHIELD_TYPE, SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def generate_obstacles(self):
        obstacles_type ={
            0: SmallCactus(SMALL_CACTUS[0]),
            1: SmallCactus(SMALL_CACTUS[1]),
            2: SmallCactus(SMALL_CACTUS[2]),
            3: LargeCactus(LARGE_CACTUS[0]),
            4: LargeCactus(LARGE_CACTUS[1]),
            5: LargeCactus(LARGE_CACTUS[2]),
            6: Bird(BIRD[0])
        } 
        return obstacles_type[random.randint(0,6)]

    def update(self, game):
        if len(self.obstacles) == 0 and game.player.type == DEFAULT_TYPE:
            self.obstacles.append(self.generate_obstacles())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.type == SHIELD_TYPE:
                print("shield activated, no damege received")
            elif game.player.dino_rect.colliderect(obstacle.rect):
                game.player.dead()
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def remove_obstacles(self):
        self.obstacles = []