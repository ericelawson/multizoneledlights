# Multi-Zone LED Lighting system

This project was created to provide AWS cloud IoT connected solution to one or more Raspberry PI Pico W controllers, each connected to WS2812 LED strips (aka Neopixels).

While there are multiple projects available to drive WS2812 lights, the attempt for this is to create the ability to run one or more LED strips in series, and address portions of those lights as "zones", with each zone being uniquely controlled and rendered to.

Each zone will contain an index of the start and end LEDs for the zone, and then it can define a static color for the zone, or a custom renderer that will be used to create custom LED effects.

The configuration for the LED renderer is based on a JSON config. It consists of the top level config object that defines the total number of LEDs in the strip, and then an array of zones, each of which index a specific LED start and end, and a color and/or renderer.

    {
        "ledcount": 10,
        "zones": [
            {
                "name": "Zone One",
                "start": 0,
                "end": 4,
                "renderer": "rainbow"
            },
            {
                "name": "Zone Two",
                "start": 5,
                "end": 9,
                "color": {
                    "red": 255,
                    "green": 0,
                    "blue": 0
                }
            }
        ]
    }

As this project progresses, I will continue to add more related to AWS configuration and setup, as well as a mobile app that will use AWS to communicate with each of the controllers.


## Hardware setup
The hardware being used is this:
 - Raspberry PI Pico W  (W indicates WiFi support) - https://www.amazon.com/Raspberry-Pre-Soldered-Official-Dual-core-Processor/dp/B0BK9W4H2Q/
 - 5v 3A (or greater) power supply with screw on terminal block - e.g. https://www.amazon.com/ALITOVE-100V-240V-Converter-5-5x2-1mm-Security/dp/B078RXZM4C/?th=1
 - PI Breakout board with headers - https://www.amazon.com/dp/B091F7YSCD
 - SN74AHCT125N IC - this converts the 3.3v output of the PI to 5v needed by the WS2812 - https://www.amazon.com/Bridgold-SN74AHCT125N-Quadruple-3-State-Outputs/dp/B08R6BCSYC/
 - WS2812 LED strip - there are many styles and types available online
 - A available 802.11n (2.4 ghz) Wifi source