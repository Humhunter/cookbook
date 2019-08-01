#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/8/1 14:34


class Lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


# example use
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @Lazyproperty
    def area(self):
        print('Counting  area')
        return math.pi * self.radius ** 2

    @Lazyproperty
    def perimeter(self):
        print('Counting perimeter')
        return 2 * math.pi * self.radius


def lazyproperty_method(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


class CircleMethod:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty_method
    def area(self):
        print('Counting  area')
        return math.pi * self.radius ** 2

    @lazyproperty_method
    def perimeter(self):
        print('Counting perimeter')
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4.0)
    print(c.radius)
    # print 仅仅打印一次
    print(c.area)
    print(c.area)
    # print 仅仅打印一次
    print(c.perimeter)
    print(c.perimeter)
    c = Circle(5.0)
    print(vars(c))
    c.area
    print(vars(c))
    c.area = 520
    print(c.area)
    c.perimeter
    print(vars(c))
    c = CircleMethod(5)