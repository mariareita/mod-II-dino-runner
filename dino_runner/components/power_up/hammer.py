from dino_runner.components.power_up.power_up import PowerUp
from dino_runner.utils.constants import HAMMER


class Hammer(PowerUp):

    def __init__(self, image):
        super().__init__(image)
        self.type = HAMMER