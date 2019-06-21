#! /usr/bin/env python
# -*- coding: utf-8 -*-
# auther : xiaojinsong(61627515@qq.com)


from itertools import permutations, combinations

if __name__ == '__main__':
    items = ['a', 'b', 'c']
    for p in permutations(items):
        print(p)
    for p in permutations(items, 2):
        print(p)
    for c in combinations(items, 3):
        print(c)
    for c in combinations(items, 2):
        print(c)