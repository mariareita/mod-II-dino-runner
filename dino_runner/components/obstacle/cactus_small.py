from dino_runner.components.obstacle.obstacle import obstacle


class SmallCactus(obstacle):
    
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 325