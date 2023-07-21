from typing import Tuple

from src.colors import BLACK
from src.lane_managers.AbstractLaneAnimation import AbstractLaneAnimation, Frame


class PixelChaseLaneAnimation(AbstractLaneAnimation):

    def __init__(self, pixel_color: Tuple, total_leds: int):
        self.pixel_color: Tuple = pixel_color
        self.total_leds: int = total_leds
        self.state: Frame = [BLACK] * total_leds
        self.active_pixel: int = 0

    def get_state(self) -> Frame:
        return self.state

    def advance_animation(self):
        self.state = [BLACK] * self.total_leds
        if self.active_pixel < self.total_leds:
            self.state[self.active_pixel] = self.pixel_color
            self.active_pixel += 1
