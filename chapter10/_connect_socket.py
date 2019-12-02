#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/11/13 14:03


from socket import socket, AF_INET, SOCK_STREAM


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'xiaojs')
s.recv(8192)
