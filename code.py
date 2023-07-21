import board
import neopixel

from src.colors import PURPLE, GREEN
from src.lane_animations.PixelChaseLaneAnimation import PixelChaseLaneAnimation
from src.track_animator.TrackAnimator import TrackAnimator

lane_1_animation = PixelChaseLaneAnimation(PURPLE, 12)
lane_2_animation = PixelChaseLaneAnimation(GREEN, 13)
lane_3_animation = PixelChaseLaneAnimation(PURPLE, 15)
lane_4_animation = PixelChaseLaneAnimation(GREEN, 18)

animator = TrackAnimator(lane_1_animation, lane_2_animation, lane_3_animation, lane_4_animation)

lane_1 = neopixel.NeoPixel(board.D10, 12, auto_write=False)
lane_2 = neopixel.NeoPixel(board.D9, 13, auto_write=False)
lane_3 = neopixel.NeoPixel(board.D6, 15, auto_write=False)
lane_4 = neopixel.NeoPixel(board.D5, 18, auto_write=False)
lanes = [lane_1, lane_2, lane_3, lane_4]

while True:
    # TODO: add in some state machine logic to control intervals
    animator.tick()
    for lane_index, lane in enumerate(animator.lane_states()):
        for i, state in enumerate(lane):
            lanes[lane_index][i] = state
    [lane.show() for lane in lanes]
