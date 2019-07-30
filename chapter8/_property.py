#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/30 8:34

import math


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class Personed:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    def delete_first_name(self):
        raise AttributeError("Can't delete attribute")

    name = property(get_first_name, set_first_name, delete_first_name)


class Circle:
    '''
    property 还是一种定义动态计算 attribute 的方法。这种类型的 attributes 并不会
被实际的存储，而是在需要的时候计算出来
    '''

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    a = Person('Guide')
    print(a.first_name)
    try:
        a.first_name = 42
    except TypeError as e:
        print(e)
    a.first_name = 'xiao'
    print(a.first_name)
    c = Circle(4.0)
    print(c.radius, c.area, c.diameter, c.perimeter, sep='\n')