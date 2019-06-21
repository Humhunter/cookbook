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
    print(ax * 2)
    print(ax + 10, ax + bx, ax * bx)


def numpy_index():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    print('# select row 1: {}'.format(a[1]))
    print('# select column 1: {}'.format(a[:, 1]))
    print('# select a subregion and change it: {} and {}'.format(a[1:3, 1:3], a[1:3, 1:3] + 10))


def numpy_matrix():
    m = np.asmatrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print(m)
    print(m.T)


if __name__ == '__main__':
    list_algorithm()
    numpy_algorithm()
    numpy_index()
    numpy_matrix()
