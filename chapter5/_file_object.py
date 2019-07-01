#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/26 9:15


import os
from socket import socket, AF_INET, SOCK_STREAM
from tempfile import TemporaryFile, TemporaryDirectory


def echo_client(client_sock, addr):
    print('Got connection from', addr)

    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
    client_out = open(client_sock.fileno, 'wt', encoding='latin-1', closefd=False)

    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)
