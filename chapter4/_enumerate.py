#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/19 14:13


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split(':')
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error {}'.format(lineno, e))


if __name__ == '__main__':
    mylist = ['a', 'b', 'c']
    for idx, val in enumerate(mylist, 1):
        print(idx, val)
