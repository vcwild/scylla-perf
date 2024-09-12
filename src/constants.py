import os


DEFAULT_HOST_IP = "172.22.0.2"
HOST_IP = os.getenv("HOST_IP", DEFAULT_HOST_IP)


class Color:
    YELLOW = "\033[33m"
    RED = "\033[31m"
    BOLD = "\033[1m"
    END = "\033[0m"
