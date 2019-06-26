#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/25 18:50


from functools import partial


def iter_partial():
    RECORD_SIZE = 32
    with open('somefile1.txt', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'') # 文本文件是逐行读取的，默认的迭代行为
        for r in records:
            print(r)


if __name__ == '__main__':
    iter_partial()