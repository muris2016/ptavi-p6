#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys


if len(sys.argv) != 3:
    sys.exit('Usage: python client.py method receiver@IP:SIPport')

METHOD = sys.argv[1]
LOGIN = sys.argv[2].split('@')[0]
IP = sys.argv[2].split('@')[1].split(':')[0]
PORT = int(sys.argv[2].split(':')[-1])

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))

MSG = '%s sip:%s@%s SIP/2.0\r\n\r\n' % (METHOD, LOGIN, IP)
print(MSG)
my_socket.send(bytes(MSG, 'utf-8'))

data = my_socket.recv(1024).decode('utf-8')

print(data)
if '100 Trying' in data and '180 Ring' and data and '200 OK' in data:
    MSG = 'ACK sip:%s@%s SIP/2.0\r\n\r\n' % (LOGIN, IP)
    my_socket.send(bytes(MSG, 'utf-8'))

print("Finishing socket...")

my_socket.close()
print("End.")
