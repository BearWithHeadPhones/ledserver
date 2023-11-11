from rpi_ws281x import PixelStrip, Color
from utils.logging import ( logger )

# LED strip configuration
LED_COUNT = 200  # Number of LEDs on your strip
LED_PIN = 18    # GPIO pin connected to the data input of the LED strip
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 150

class LedStrip:
    def __init__(self):
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, False, LED_BRIGHTNESS)
        self.strip.begin()
        logger.debug("initialized")
   
    def set_color_of_entire_strip(self,color):
        logger.debug("setting color")
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
        self.strip.show()    






