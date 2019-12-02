#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/10/16 18:32


import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profiled
def add(x ,y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


if __name__ == '__main__':
    print(add(2, 3))
    print(add(4, 5))
    print(add.ncalls)
