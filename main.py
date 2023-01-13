import wlan
import ledrenderer
import json
from models.deserializer import create_config
from models.config import config
from models.zone import zone
from models.color import color

def main():
    # load configuration
    configFile = open('config.json')
    c = create_config(json.load(configFile))

    print('renderer starting')
    renderer = ledrenderer.ledrenderer(c.ledcount)
    
    # While initializing, render a single blue color
    renderer.clear_all()
    renderer.render([zone('init', 0, c.ledcount - 1, color(0,0,255))])

    # Connect to WiFi
    wlan.init_wlan()

    # now begin rendering based on config
    while(True):
        renderer.render(c.zones)

if __name__ == "__main__":
    main()

