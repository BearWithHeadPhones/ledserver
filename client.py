import grpc
import led_controller_pb2_grpc
import ColorRequest_pb2
import time


def run_client():
    channel = grpc.insecure_channel("localhost:50052")
    stub = led_controller_pb2_grpc.LEDControllerStub(channel)

    colors = ["0x000000","0xff00ff","0x00FFFF", "0xFFFF00"]
    while True:
        for color in colors:
            color_request = ColorRequest_pb2.ColorRequest(color=color)
            response = stub.SetColor(color_request)
            print(response)
            time.sleep(1)
        

if __name__ == "__main__":
    run_client()