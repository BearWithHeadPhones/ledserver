import led_controller_pb2
import led_controller_pb2_grpc
from utils.logging import ( logger )


class LEDControllerServicer(led_controller_pb2_grpc.LEDControllerServicer):
    def __init__(self,handler):
        self.handler = handler
        logger.debug("initialized")

    def SetColor(self, request, context):
        logger.debug(f"received request: {request}")
        try:
            self.handler.handle(request)
            return led_controller_pb2.ColorResponse(status="Color set successfully")
        except Exception as e:
            return led_controller_pb2.ColorResponse(status=f"Error: {str(e)}")