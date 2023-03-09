import random
from dino_runner.components.power_up.hammer import Hammer
from dino_runner.components.power_up.heart import Heart
from dino_runner.components.power_up.shield import Shield
from dino_runner.utils.constants import DEFAULT_TYPE, HAMMER, HEART, SHIELD


class PowerUpManager:
    POWER_UP_PROBABILITY = 2

    def __init__(self):
        self.power_ups = []

    def generate_power_up(self):
        if random.randint(0, 100) < self.POWER_UP_PROBABILITY:
            self.power_ups.append(Shield(SHIELD))
        elif random.randint(0, 100) < self.POWER_UP_PROBABILITY:
            self.power_ups.append(Hammer(HAMMER))
        elif random.randint(0, 100) < self.POWER_UP_PROBABILITY:
            self.power_ups.append(Heart(HEART))
        

    def update(self, game):
        if len(self.power_ups) == 0 and game.player.type == DEFAULT_TYPE:
            self.generate_power_up()
            

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                game.player.activate_power_up(power_up.type)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def remove_power_ups(self):
        self.power_ups = []

