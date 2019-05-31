#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/31 18:16


from collections import ChainMap


def chain_operate():
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}

    # 如果出现重复键，那么第一次出现的映射值会被返回
    c = ChainMap(a, b)
    print(c, type(c))
    print(c.keys(), list(list(c.keys())), len(c), c.values(), list(c.values()))
    print(c['x'], c['y'], c['z'])
    d = ChainMap(b, a)
    print(d['x'], d['y'], d['z'])

    # 更新或者删除操作
    c['z'] = 10
    c['w'] = 40
    c['j'] = 50
    del c['x']
    print(a, b)

    # 作用域问题
    values = ChainMap()
    values['x'] = 1
    values = values.new_child()
    values['x'] = 2
    values = values.new_child()
    values['x'] = 3
    print(values)
    print(values['x'])

    # discard last mapping
    values = values.parents
    print(values['x'])
    values = values.parents
    print(values['x'])


if __name__ == '__main__':
    chain_operate()
