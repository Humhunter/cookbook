#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/19 14:13

from itertools import zip_longest


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split(':')
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error {}'.format(lineno, e))


def meanwhile_zip():
    xpts = [1, 5, 4, 2, 10, 9]
    ypts = [101, 78, 32, 16, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)


def combine_zip():
    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a, b):
        print(i)
    for i in zip_longest(a, b):
        print(i)
    for i in zip_longest(a, b, fillvalue=0):
        print(i)


def dict_zip():
    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    s = dict(zip(headers, values))
    for name, val in zip(headers, values):
        print(name, '=', val)


if __name__ == '__main__':
    mylist = ['a', 'b', 'c']
    for idx, val in enumerate(mylist, 1):
        print(idx, val)
    meanwhile_zip()
    combine_zip()
    dict_zip()