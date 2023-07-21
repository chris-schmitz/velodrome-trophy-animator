from typing import Tuple

from src.lane_managers.AbstractLaneAnimation import AbstractLaneAnimation, Frame


class FrameAnimation(AbstractLaneAnimation):
    def __init__(self, total_leds: int, *frames: Frame):
        self.total_leds: int = total_leds
        self.frames: Tuple[Frame] = frames
        self.active_frame: int = 0

    def advance_animation(self):
        if self.active_frame + 1 >= len(self.frames):
            self.active_frame = 0
        else:
            self.active_frame += 1

    def get_state(self) -> Frame:
        return self.frames[self.active_frame]
