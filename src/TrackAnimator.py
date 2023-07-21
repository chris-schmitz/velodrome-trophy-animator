# ! TrackAnimator
# * This class manages the passage of time for the animations and is
# * meant to be used with a higher level state machine that determines
# * the intervals between ticks.
from typing import List

from src.lane_managers.AbstractLaneAnimation import AbstractLaneAnimation, Frame


class TrackAnimator:
    def __init__(self, *lane_animations: AbstractLaneAnimation):
        self.lane_animations = list(lane_animations)

    def lane_states(self) -> List[Frame]:
        return [animation.get_state() for animation in self.lane_animations]

    def tick(self):
        for lane_animation in self.lane_animations:
            lane_animation.advance_animation()

    def set_config(self, lane_index: int, animation):
        self.lane_animations[lane_index] = animation
