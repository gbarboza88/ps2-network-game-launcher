#!/usr/bin/env python3
import argparse
import socket
import struct
import os

MAGIC = 0x0000EA6E

def main(args):
    # Get filesize
    stats = os.stat(args.file)

    # Connect to console
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    sock.connect((args.ip, args.port))

    # Send magic
    sock.sendall(struct.pack('<I', MAGIC))

    # Send filesize
    sock.sendall(struct.pack('<Q', stats.st_size))

    # Send file
    with open(args.file, 'rb') as file:

        # Loop in chunks of 4096
        while True:
            data = file.read(4096)
            if data == b'':
                break
            sock.sendall(data)

    sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a file over TCP.')
    parser.add_argument('-i', '--ip', required=True, help='The target IP address.')
    parser.add_argument('-p', '--port', type=int, default=9045, help='The target port number.')
    parser.add_argument('-f', '--file', required=True, help='The file to send.')
    main(parser.parse_args())