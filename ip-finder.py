import socket
import re
import time
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s\t%(message)s")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("", 37001))
    sock.settimeout(2)

    logging.info("Start.")
    while True:
        try:
            msg, address = sock.recvfrom(256)
            logging.info("Receive Packet from %s %s", msg.decode('utf8'), address[0])

        except socket.timeout:
            pass
        except (KeyboardInterrupt, SystemExit):
            break
        except:
            logging.exception("error")


if __name__ == "__main__":
    main()
