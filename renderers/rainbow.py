from neopixel import NeoPixel
from renderers.customrenderer import custom_renderer

"""
Rainbow custom renderer. This will create a rainbow chasing effect across the zone. This was inspired from the effect found here:
https://www.tweaking4all.com/hardware/arduino/adruino-led-strip-effects/#LEDStripEffectRainbowCycle
"""
class rainbow_renderer(custom_renderer):
    wheel_position = 0
    
    def render(self, start:int, end: int, pixels: NeoPixel):
        # calculate the current position of the color wheel used to calculate the current list of colors
        if self.wheel_position == 256*5:
            self.wheel_position = 0
        else:
            self.wheel_position = self.wheel_position + 1
            
        # calculate the total number of LEDs in the zone
        zone_led_count = end - start
        
        # calculate color for each LED and write to each pixel
        for i in range(start, end + 1):
            color: tuple = self.colorwheel((round((i * 256 / zone_led_count) + self.wheel_position)) & 255)
            pixels[i] = color
            print('rainbow: setting color for led [' + str(i) + '] to ' + str(pixels[i])) 
        
    """
    calculates the color of a pixel based on a calculated location from 0-255 on a colorwheel. 
    """
    def colorwheel(self, position: int) -> tuple:
        if(position < 85):
            return (
                position * 3,
                255 - position * 3,
                0
            )
        elif(position < 170):
            position -= 85
            return (
                255 - position * 3,
                0,
                position * 3
            )
        else:
            position -= 170
            return (
                0,
                position * 3,
                255 - position * 3
            )
  