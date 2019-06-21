#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/20 20:03


if __name__ == '__main__':
    f = open('passwd.txt')
    for chunk in iter(lambda: f.read(10), ''):
        print(chunk)
