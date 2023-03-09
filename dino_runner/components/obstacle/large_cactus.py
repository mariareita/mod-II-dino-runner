from dino_runner.components.obstacle.obstacle import obstacle


class LargeCactus(obstacle):
    
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 300