import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="ledserver aruments")
    parser.add_argument("--port", type=str, default="50052", help="grpc port")

    args = parser.parse_args()
    return args