from models.zone import zone
import neopixel
import machine
import time

class ledrenderer:

    SLEEP_INTERVAL_MS = 1000

    def __init__(self, pixelcount: int):
        self.pixelcount = pixelcount
        print('initializing LED strip')
        self.pixels = neopixel.NeoPixel(machine.Pin(22), self.pixelcount)
        self.clear_all()

    def clear_all(self):
        print('clearing all pixels in LED strip')
        self.pixels.fill((0,0,0))
        self.pixels.write()
        time.sleep_ms(self.SLEEP_INTERVAL_MS)

    def render(self, zones: list[zone]):
        for zone in zones:
            #print('rendering zone ' + zone.name)
            zone.render(self.pixels)    
        print('writing to LED strip')
        self.pixels.write()
        time.sleep_ms(self.SLEEP_INTERVAL_MS)
        