from Obstacle import *

# Class that specifies the properties of the stairs.
class Stair(Obstacle):
    def __init__(self, pos, width, height) -> None:
        super().__init__(pos, width, height, "sprites/stair.png")

    # Rendering method
    def draw(self, screen):
        screen.blit(self._image, self.pos)

    def is_instance_at_stair(self, who_interval, direction):
        if direction == "up":
                stair_interval = self._get_position_interval()
                if who_interval[0][0] <= stair_interval[1][0] and who_interval[1][0] >= stair_interval[0][0]:
                    if who_interval[1][1] + 2 >= stair_interval[0][1] and who_interval[1][1] - 2 <= stair_interval[1][1]:
                        return True
        elif direction == "down":
                stair_interval = self._get_position_interval()
                if who_interval[0][0] <= stair_interval[1][0] and who_interval[1][0] >= stair_interval[0][0]:
                    if who_interval[1][1] - 2 <= stair_interval[0][1]:
                        return True
                    
    def is_alien_at_stair(self, alien_interval):
        stair_interval = self._get_position_interval()
        if ((alien_interval[0][0] + alien_interval[1][0]) // 2) == ((stair_interval[1][0] + stair_interval[0][0]) // 2):
            if alien_interval[1][1] - 2 >= stair_interval[0][1] and alien_interval[0][1] + 2 <= stair_interval[1][1]:
                 return True
        return False