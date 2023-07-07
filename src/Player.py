from Character import *

# Class that specifies the properties of the player. Also has the control methods.
class Player(Character):
    def __init__(self, x, y, width, height, sprites: dict, state: str) -> None:
        super().__init__(x, y, width, height, sprites, state)

    def climb_down(self):
        self.fall()

    def climb_up(self):
        self.y -= 2

    def jump(self):
        self.y -= 2

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def fall(self):
        self.y += 1

    def move_up_platforms(self):
        self.y -= 2

    def is_at_step(self, platform, side: str):
        if platform.is_instance_at_step(self._get_position_interval(), side):
            self.move_up_platforms()

    def did_hit_rock(self, rock):
        return rock.did_player_hit_rock(self._get_position_interval())
    
    def did_hit_alien(self, alien):
        return alien.did_player_hit_alien(self._get_position_interval())
    
    def did_collide_with_spacebro(self, spacebro):
        return spacebro.did_player_collide(self._get_position_interval())
    
    def is_on_platform(self, platform):
        return platform.is_not_on_platform(self._get_position_interval())
    
    def did_fall(self):
        return self._get_position_interval()[0][1] >= 720
    
    def is_at_stairs(self, stair, direction):
        return stair.is_instance_at_stair(self._get_position_interval(), direction)
