from Obstacle import *
import Alien

# Class that specifies the properties of oil drum.
class AlienSpaceship(Obstacle):
    def __init__(self, pos, width, height) -> None:
        self.sprites = ["sprites/spaceship-1.png", "sprites/spaceship-2.png"]
        super().__init__(pos, width, height, "sprites/spaceship-1.png")

    def deploy_alien(self):
        pass

    # Rendering method
    def draw(self, screen, frame):
        self._imagetemplate = pg.image.load(self.sprites[frame % (len(self.sprites))])
        self._image = pg.transform.scale(self._imagetemplate, self.size)
        self._rect = self._image.get_rect()
        screen.blit(self._image, self.pos)