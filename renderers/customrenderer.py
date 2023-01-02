from neopixel import NeoPixel

"""
Base class that all custom renderers must subclass
"""
class custom_renderer:
    def render(self, start: int, end:int, pixels: NeoPixel):
        pass