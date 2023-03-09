import random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud:
    X_POS = 1500
    Y_POS = 150

    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            self.rect.x = self.X_POS

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))