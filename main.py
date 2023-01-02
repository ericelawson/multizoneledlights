import wlan
import ledrenderer
import json
from models.deserializer import create_config
from models.config import config
from models.zone import zone
from models.color import color

def main():
    # Connect to WiFi
    wlan.init_wlan()

    # load configuration
    configFile = open('config.json')
    c = create_config(json.load(configFile))

    print('renderer starting')
    renderer = ledrenderer.ledrenderer(c.ledcount)

    while(True):
        renderer.render(c.zones)

if __name__ == "__main__":
    main()

