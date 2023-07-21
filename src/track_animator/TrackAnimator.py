# ! TrackAnimator
# * This class manages the passage of time for the animations and is
# * meant to be used with a higher level state machine that determines
# * the intervals between ticks.


# TODO: consider expansion
# * one of the things we know we're going to want to do is switch animations based on some physical event. Should we
# * handle that in this class or outside of it? Implications being that we'd need to accept _all_ of the different
# * animation styles (e.g. Pixel chases AND frame animations) within the class instance.
# * This is as opposed to handling it outside of the class and just facilitating the ability to set new animations on
# * the fly.
# ! I think it's arguable that we could do that in here, but let's get it working outside of the class first and then
# ! reconsider the question.
class TrackAnimator:
    def __init__(self, *lane_animations):
        self.lane_animations = list(lane_animations)

    def lane_states(self):
        return [animation.get_state() for animation in self.lane_animations]

    def tick(self):
        for lane_animation in self.lane_animations:
            lane_animation.advance_animation()

    def set_config(self, lane_index: int, animation):
        self.lane_animations[lane_index] = animation
