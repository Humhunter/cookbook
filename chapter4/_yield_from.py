#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/20 9:22


from collections import Iterable


def flatten_grace(items, ignore_types=(str, bytes)):
    '''
    你想将一个多层嵌套的序列展开成一个单层列表，更加优雅
    :param items:
    :param ignore_types:
    :return:
    '''
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten_grace(x)
        else:
            yield x


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x


if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items):
        print(x)
    for x in flatten_grace(items):
        print(x)