from utils.logging import ( logger )

class SetColor:
    def __init__(self, hardware_abstraction_layer):
        self.hardware_abstraction_layer = hardware_abstraction_layer


    def handle(self, request):
        logger.debug("handling request")
        color = request.color
        if color:
            color_hex = int(color, 16)
            self.hardware_abstraction_layer.set_color_of_entire_strip(color_hex)
            