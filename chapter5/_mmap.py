#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/25 18:58


import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


if __name__ == '__main__':
    size = 10000
    with open('data', 'wb') as f:
        f.seek(size -1)
        f.write(b'\x00')
    m = memory_map('data')
    print(len(m), m[0:10], m[0])
    m[0:11] = b'hello world'
    m.close()
    with open('data', 'rb') as f:
        print(f.read(11))
