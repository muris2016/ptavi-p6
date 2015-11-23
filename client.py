#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

if __name__ == "__main__":
    METHOD = sys.argv[1]
    LOGIN = sys.argv[2].split('@')[0]
    IP = sys.argv[2].split('@')[1].split(':')[0]
    PORT = int(sys.argv[2].split(':')[-1])

    if METHOD == 'INVITE' or METHOD == 'BYE':
        MSG = '%s sip:%s@%s SIP/2.0\r\n\r\n' % (METHOD, LOGIN, IP)
        print(MSG)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((IP, PORT))
    
    my_socket.send(bytes(MSG, 'utf-8'))

    data = my_socket.recv(1024)

    print(data.decode('utf-8'))
    print("Finishing socket...")

    my_socket.close()
    print("End.")
