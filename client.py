import grpc
import led_controller_pb2
import led_controller_pb2_grpc


def run_client():
    channel = grpc.insecure_channel("localhost:50052")
    stub = led_controller_pb2_grpc.LEDControllerStub(channel)
    color_request = led_controller_pb2.ColorRequest(color="0xff00ff") #magenta
    response = stub.SetColor(color_request)
    print(response)


if __name__ == "__main__":
    run_client()