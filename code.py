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
lane_2 = neopixel.NeoPixel(board.D9, 12, auto_write=False)
lane_3 = neopixel.NeoPixel(board.D6, 12, auto_write=False)
lane_4 = neopixel.NeoPixel(board.D5, 12, auto_write=False)

while True:
    for i, state in enumerate(animator.lane_states()[0]):
        lane_1[i] = state[i]

    # lane_2 = animator.lane_states()[1]
    # lane_3 = animator.lane_states()[2]
    # lane_4 = animator.lane_states()[3]
