#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/4 12:40

text = 'Hello World'

def str_align():
    print(text.ljust(20))
    print(text.rjust(20))
    print(text.center(20))
    print(text.ljust(20, '*'))
    print(text.rjust(20, '*'))
    print(text.center(20, '*'))


def str_format():
    print(format(text, '>20'))
    print(format(text, '<20'))
    print(format(text, '^20'))
    print(format(text, '=>20'))
    print(format(text, '=<20'))
    print(format(text, '=^20'))
    print('{:>10} {:>10}'.format('hello', 'world'))


if __name__ == '__main__':
    str_align()
    str_format()