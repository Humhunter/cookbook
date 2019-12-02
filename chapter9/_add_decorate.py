#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/8/20 19:54


import time
from functools import wraps
from inspect import signature


def timethis(func):
    '''
    Decorator that reports the execution time.
    :param func:
    :return:
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    print('Begin count')
    while n > 0:
        n -= 1


if __name__ == '__main__':
    countdown(100000000)
    print(countdown.__wrapped__(100000))
    print(signature(countdown))