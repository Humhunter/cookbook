#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/24 8:53


import io


if __name__ == '__main__':
    s = io.StringIO()
    s.write('Hello World\n')
    print('This is test', file=s)
    print(s.getvalue())
    s = io.StringIO('Hello\nWorld\n')
    print(s.read(4))
    print(s.read())