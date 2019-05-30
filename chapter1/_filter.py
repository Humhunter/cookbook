#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/30 18:06


def common_filter():
    '''
    列表推导式
    :return:
    '''
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    resultList = [n for n in mylist if n > 0]


values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


# filter 得到的是迭代器
ivals = list(filter(is_int, values))
print(ivals)

from itertools import compress

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
