from neopixel import NeoPixel
import machine

class ledwriter:
    def __init__(self, ledcount: int):
        self.ledcount = ledcount
        # initialize NeoPixel strip
        self.pixels = NeoPixel(machine.Pin(28), ledcount)
    
    def setAll(self, color: tuple):
        self.pixels.fill(color)
        
    def setPixel(self, index: int, color: tuple):
        self.pixels[index] = color
        
    def write(self):
        self.pixels.write()