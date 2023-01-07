from neopixel import NeoPixel

class ledwriter:
    def __init__(self, ledcount: int, pixels: NeoPixel):
        self.ledcount = ledcount
        self.pixels = pixels
    
    def setAll(self, color: tuple):
        self.pixels.fill(color)
        
    def setPixel(self, index: int, color: tuple):
        self.pixels[index] = color
        
    def write(self):
        self.pixels.write()