from Obstacle import *
import Alien

# Class that specifies the properties of oil drum.
class AlienSpaceship(Obstacle):
    def __init__(self) -> None:
        super().__init__()

    def deploy_alien(self):
        pass

    def draw(self, screen):
        screen.blit(self._image, self.pos)