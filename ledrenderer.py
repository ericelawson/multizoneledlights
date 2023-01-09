from models.zone import zone
import neopixel
import machine
import time
from ledwriter import ledwriter

class ledrenderer:

    SLEEP_INTERVAL_MS = 20

    def __init__(self, pixelcount: int):
        self.pixelcount = pixelcount
        print('initializing LED strip')
        self.writer = ledwriter(pixelcount)
        self.clear_all()

    def clear_all(self):
        print('clearing all pixels in LED strip')
        self.writer.setAll((0,0,0))
        self.writer.write()
        time.sleep_ms(self.SLEEP_INTERVAL_MS)

    def render(self, zones: list[zone]):
        for zone in zones:
            zone.render(self.writer)    
        self.writer.write()
        time.sleep_ms(self.SLEEP_INTERVAL_MS)        