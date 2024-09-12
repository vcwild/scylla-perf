from src.utils import find_host_ip
import os

HOST_IP = os.getenv("HOST_IP", find_host_ip())
