from Obstacle import *
import Alien

# Class that specifies the properties of oil drum.
class AlienSpaceship(Obstacle):
    def __init__(self, pos, width, height) -> None:
        super().__init__(pos, width, height, "sprites/spaceship.png")

    def deploy_alien(self):
        pass

    # Rendering method
    def draw(self, screen):
        screen.blit(self._image, self.pos)