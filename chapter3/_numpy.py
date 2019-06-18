#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/13 8:25


import numpy as np


def list_algorithm():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2)
    try:
        x + 10
    except Exception as e:
        print(e)
    finally:
        print(x + y)


def numpy_algorithm():
    ax = np.array([1, 2, 3, 4])
    bx = np.array([5, 6, 7, 8])


if __name__ == '__main__':
    list_algorithm()
