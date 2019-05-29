#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/27 18:53


from collections import defaultdict
from collections import OrderedDict


def set_multidict():
    '''
    一个键对应多个值
    :return:
    '''
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    e = defaultdict(set)
    e['a'].add(1)
    e['a'].add(2)
    e['b'].add(4)
    print(type(d), d, type(e), e)


def set_ordered_dict():
    '''
    在迭代操作的时候它会保持元素被插入时的顺序
    :return: None
    '''
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 4
    d['grok'] = 3
    print(d)


def algorithm_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    print(min_price, max_price)
    print(min(prices), min(prices.values()), min(prices, key=lambda k: prices[k]))


def find_similarity_dict():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }
    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(b.keys() - a.keys())
    print(a.items() & b.items())


if __name__ == '__main__':
    set_multidict()
    set_ordered_dict()
    algorithm_dict()
    find_similarity_dict()