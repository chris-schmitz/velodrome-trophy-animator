from src.colors import RED, BLACK, GREEN, BLUE
from src.lane_animations.FrameAnimation import FrameAnimation
from src.lane_animations.PixelChaseLaneAnimation import PixelChaseLaneAnimation
from src.track_animator.TrackAnimator import TrackAnimator


class TestSuite:

    def test_pixel_chase_animation___can_initialize_pixel_chase_and_tick_a_couple_of_times(self):
        animator = TrackAnimator(PixelChaseLaneAnimation(total_leds=10, pixel_color=RED))

        assert animator.lane_states()[0] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

        animator.tick()
        assert animator.lane_states()[0] == [RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

        animator.tick()
        assert animator.lane_states()[0] == [BLACK, RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

    def test_pixel_chase_animation___can_roll_over_pixel_chase(self):
        animator = TrackAnimator(PixelChaseLaneAnimation(RED, 10))

        assert animator.lane_states()[0] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

        [animator.tick() for _ in range(10)]

        assert animator.lane_states()[0] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED]

    def test_pixel_chase_animation___run_more_than_one_lane(self):
        animator = TrackAnimator(
            PixelChaseLaneAnimation(RED, 10),
            PixelChaseLaneAnimation(GREEN, 15)
        )

        assert animator.lane_states()[0] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
        assert animator.lane_states()[1] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
                                             BLACK, BLACK,
                                             BLACK, BLACK, BLACK]

        [animator.tick() for _ in range(10)]
        assert animator.lane_states()[0] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, RED]
        assert animator.lane_states()[1] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, GREEN,
                                             BLACK, BLACK,
                                             BLACK, BLACK, BLACK]

        [animator.tick() for _ in range(5)]
        assert animator.lane_states()[0] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
        assert animator.lane_states()[1] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
                                             BLACK, BLACK,
                                             BLACK, BLACK, GREEN]

    def test_pixel_chase_animation___reset_lane_animation(self):
        magenta = (233, 12, 5)
        white = (255, 255, 255)

        animator = TrackAnimator(
            PixelChaseLaneAnimation(magenta, 10),
            PixelChaseLaneAnimation(white, 10)
        )

        assert animator.lane_states()[0] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
        assert animator.lane_states()[1] == [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

        [animator.tick() for _ in range(3)]

        assert animator.lane_states()[0] == [BLACK, BLACK, magenta, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
        assert animator.lane_states()[1] == [BLACK, BLACK, white, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

        animator.set_config(1, PixelChaseLaneAnimation(RED, 10))
        animator.tick()

        assert animator.lane_states()[0] == [BLACK, BLACK, BLACK, magenta, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
        assert animator.lane_states()[1] == [RED, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]

    def test_frame_animation___can_animate_a_single_lane(self):
        red_green_frame = [RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN]
        green_red_frame = [GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED]
        lane_animation = FrameAnimation(10, red_green_frame, green_red_frame)

        animator = TrackAnimator(lane_animation)

        assert animator.lane_states()[0] == red_green_frame
        animator.tick()
        assert animator.lane_states()[0] == green_red_frame
        animator.tick()
        assert animator.lane_states()[0] == red_green_frame

    def test_frame_animation___can_animate_multiple_lanes(self):
        red_green_frame = [RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN]
        green_red_frame = [GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED, GREEN, RED]
        blue_cycle_1 = [GREEN, GREEN, BLUE, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN]
        blue_cycle_2 = [GREEN, BLUE, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN]
        blue_cycle_3 = [BLUE, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN]
        lane_1_animation = FrameAnimation(10, red_green_frame, green_red_frame)
        lane_2_animation = FrameAnimation(10, blue_cycle_1, blue_cycle_2, blue_cycle_3)

        animator = TrackAnimator(lane_1_animation, lane_2_animation)

        assert animator.lane_states()[0] == red_green_frame
        assert animator.lane_states()[1] == blue_cycle_1

        animator.tick()
        assert animator.lane_states()[0] == green_red_frame
        assert animator.lane_states()[1] == blue_cycle_2

        animator.tick()
        assert animator.lane_states()[0] == red_green_frame
        assert animator.lane_states()[1] == blue_cycle_3

        animator.tick()
        assert animator.lane_states()[0] == green_red_frame
        assert animator.lane_states()[1] == blue_cycle_1
