#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/8/2 18:32


import math


class Structure1:
    _fileds = []

    def __init__(self, *args):
        if len(args) != len(self._fileds):
            raise TypeError('Expected {} arguments'.format(len(self._fileds)))
        for name, value in zip(self._fileds, args):
            setattr(self, name, value)


# example use
class Stock(Structure1):
    _fileds = ['name', 'shares', 'price']


class Point(Structure1):
    _fileds = ['x', 'y']


class Circle(Structure1):
    _fileds = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


class Structure2:
    _fileds = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fileds):
            raise TypeError('Expected {} arguments'.format(len(self._fileds)))

        for name, value in zip(self._fileds, args):
            setattr(self, name, value)




if __name__ == '__main__':
    s = Stock('Ace', 50, 91.1)
    p = Point(3, 4)
    c = Circle(5.0)
    print(s, p, c)
    print(c.area())
    try:
        s = Stock('yuanma', 26)
    except TypeError as e:
        print(e)
