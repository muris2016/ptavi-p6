#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def handle(self):
        audio_file = sys.argv[3]
        while 1:
            line = self.rfile.read().decode('utf-8')
            if not line:
                break
            print(line)
            if len(line.split()) != 3:
                self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")
                break

            method = line.split()[0]
            sip_login_ip = line.split()[1]
            sip_version = line.split()[2]

            if (not 'sip:' in sip_login_ip or not '@' in sip_login_ip
                    or sip_version != 'SIP/2.0'):
                self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")
                break

            if method == 'INVITE':
                self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n"
                                 + b"SIP/2.0 180 Ring\r\n\r\n"
                                 + b"SIP/2.0 200 OK\r\n\r\n")
            elif method == 'BYE':
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            elif method == 'ACK':
                os.system('./mp32rtp -i 127.0.0.1 -p 23032 < ' + audio_file)
            else:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit('Usage: python server.py IP port audio_file')
    if not os.path.exists(sys.argv[3]):
        sys.exit("File %s doesn't exist" % (sys.argv[3]))
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    serv = socketserver.UDPServer((IP, PORT), EchoHandler)
    print("Listening...")
    serv.serve_forever()
