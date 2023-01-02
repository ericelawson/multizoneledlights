from models.zone import zone

class config:
    def __init__(self, ledcount: int, zones: list[zone]):
        self.ledcount = ledcount
        self.zones = zones

    def addZone(self, zone: zone):
        self.zones.append(zone)

    def removeZone(self, index: int):
        self.zones.pop(index)

    def clearAllZones(self):
        self.zones.clear()

    def replaceAllZones(self, zones: list[zone]):
        self.zones.clear()
        self.zones = zones