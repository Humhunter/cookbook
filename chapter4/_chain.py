#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/20 8:43


from itertools import chain


def iter_chain():
    '''
    你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不
    失可读性的情况下避免写重复的循环
    '''
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print(x)
    active_items = set()
    inactive_items = set()
    for item in chain(active_items, inactive_items):
        print(item)


if __name__ == '__main__':
    iter_chain()
