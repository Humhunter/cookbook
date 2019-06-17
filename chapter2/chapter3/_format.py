#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/10 18:38


def format_decimal():
    x = 1234.5678
    print(format(x, '0.2f'))
    print(format(x, '>10.1f'))
    print(format(x, '<10.1f'))
    print(format(x, '^10.1f'))
    print(format(x, '0,.1f'))


if __name__ == '__main__':
    format_decimal()
