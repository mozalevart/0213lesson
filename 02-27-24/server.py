import socket
import logging
import json
import random
import datetime

from common import ADDR

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 10000))

while True:
    message, (ip, port) = s.recvfrom(500)
    logger.info(f"{ip}: {message.decode()}")
    if message.decode() == "quit":
        quit()


'''while True:
    try:
        client_socket = s.accept()
    except TimeoutError:
        continue
    client, (addr, port) = client_socket
    logger.warning(f"{addr} connected from port {port}")

    data = {
        "time": datetime.datetime.now().isoformat(),
        "number": random.random()
        }

    client.send(json.dumps(data).encode())
    # b''.decode()
    # "".encode()
    client.close()
    
    '''



