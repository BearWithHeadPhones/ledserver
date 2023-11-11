import grpc
from concurrent import futures
import led_controller_pb2_grpc
from server.LEDControllerServicer import (LEDControllerServicer)
from utils.logging import ( logger )
from server.handlers.SetColor import (SetColor)
from HAL.LedStrip import (LedStrip)

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    led_controller_pb2_grpc.add_LEDControllerServicer_to_server(LEDControllerServicer(SetColor(LedStrip())), server)
    server.add_insecure_port(f"localhost:{port}")
    server.start()
    logger.debug(f"gRPC server is running on port {port}...")
    server.wait_for_termination()