class FrameAnimation:
    def __init__(self, total_leds: int, *frames):
        self.total_leds: int = total_leds
        self.frames = frames
        self.active_frame: int = 0

    def advance_animation(self):
        if self.active_frame + 1 >= len(self.frames):
            self.active_frame = 0
        else:
            self.active_frame += 1

    def get_state(self):
        return self.frames[self.active_frame]
