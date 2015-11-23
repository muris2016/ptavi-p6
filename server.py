#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
            line = self.rfile.read().decode('utf-8').split()
            if not line:
                break
            if 'INVITE' in line:
                self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\nSIP/2.0 180 Ring\r\n\r\nSIP/2.0 200 OK\r\n\r\n")
            else:
                self.wfile.write(b"SIP/2.0 400 BAD REQUEST\r\n\r\n")


if __name__ == "__main__":
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    serv = socketserver.UDPServer((IP, PORT), EchoHandler)
    print("Listening...")
    serv.serve_forever()
