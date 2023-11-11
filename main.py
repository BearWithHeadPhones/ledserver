import grpc
from concurrent import futures
import led_controller_pb2
import led_controller_pb2_grpc
from rpi_ws281x import PixelStrip, Color

# LED strip configuration
LED_COUNT = 30  # Number of LEDs on your strip
LED_PIN = 18    # GPIO pin connected to the data input of the LED strip
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255

class LEDControllerServicer(led_controller_pb2_grpc.LEDControllerServicer):
    def __init__(self):
        # Initialize the LED strip
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, False, LED_BRIGHTNESS)
        self.strip.begin()

    def SetColor(self, request, context):
        color = request.color
        if not color:
            return led_controller_pb2.ColorResponse(status="Color not specified")

        try:
            # Set the color on the LED strip
            color_hex = int(color, 16)
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, color_hex)
            self.strip.show()

            return led_controller_pb2.ColorResponse(status="Color set successfully")
        except Exception as e:
            return led_controller_pb2.ColorResponse(status=f"Error: {str(e)}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    led_controller_pb2_grpc.add_LEDControllerServicer_to_server(LEDControllerServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("gRPC server is running on port 50052...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
