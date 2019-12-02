#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/11/13 11:50


from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler
import socket


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connecton from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


class EchoHandler_thead(StreamRequestHandler):
    timeout = 5
    rbufsize = -1
    wbufsize = 0
    disable_nagle_algorithm = False

    def handle(self):
        print('Got connection from', self.client_address)
        try:
            for line in self.rfile:
                self.wfile.write(line)
        except socket.timeout:
            print('Time out!!')


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
