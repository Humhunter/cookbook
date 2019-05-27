#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/27 18:53


from collections import defaultdict
from collections import OrderedDict


def set_multidict():
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
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 4
    d['grok'] = 3


if __name__ == '__main__':
    set_multidict()
