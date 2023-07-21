from src.colors import BLACK


class PixelChaseLaneAnimation:

    def __init__(self, pixel_color, total_leds: int):
        self.pixel_color = pixel_color
        self.total_leds: int = total_leds
        self.state = [BLACK] * total_leds
        self.active_pixel: int = 0

    def get_state(self):
        return self.state

    def advance_animation(self):
        self.state = [BLACK] * self.total_leds
        if self.active_pixel < self.total_leds:
            self.state[self.active_pixel] = self.pixel_color
            self.active_pixel += 1
        else:
            self.active_pixel = 0
