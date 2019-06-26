#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/24 9:00


import gzip
import bz2


if __name__ == '__main__':
    with gzip.open('somefile.gz', 'rb', compresslevel=5) as f:
        f.read()
    with bz2.open('somefile.txt', 'rt') as f:
        text = f.read()