#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/8/20 18:23


import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:}, {!r:})'.format(self.x , self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


if __name__ == '__main__':
    p = Point(2, 3)
    d = getattr(p, 'distance')(0, 0)
    print(d)