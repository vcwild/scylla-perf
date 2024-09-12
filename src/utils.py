import logging
import subprocess
import re
from time import sleep
from src.colors import Color as c


def find_host_ip() -> str:
    """Tries to find the IP address of the ScyllaDB container, else deploys a new instance of it."""
    result = subprocess.run(
        ["docker", "exec", "-it", "some-scylla", "nodetool", "status"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        output = result.stdout
        try:
            ip_addresses = re.findall(
                r"UN\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", output
            )[0]
            return ip_addresses
        except IndexError:
            pass
    logging.warning(c.YELLOW + "Starting the ScyllaDB container..." + c.END)
    subprocess.run(["docker-compose", "up", "-d"])
    sleep(5)
    return find_host_ip()
