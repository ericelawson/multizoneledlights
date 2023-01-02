from models.config import config
from models.zone import zone
from models.color import color

# Due to some of the inherent ugliness of using json.loads() to create strongly typed class objects 
# from the JSON structures, I will use this to construct the config classes from the JSON objects.

def create_config(json: dict) -> config:
    
    zones = []
    
    zones_value = json.get('zones')
    if zones_value != None:
        for zone_value in zones_value:
            color_value = zone_value.get('color')
            c = color(0,0,0)
            if color_value:
                c = color(
                    color_value.get('red'),
                    color_value.get('green'),
                    color_value.get('blue') 
                )

            z = zone(
                zone_value.get('name'),
                zone_value.get('start'),
                zone_value.get('end'),
                c,
                zone_value.get('renderer')
            )
            zones.append(z)
    
    cfg = config(
        json['ledcount'],
        zones
    )
    return cfg