#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/15 17:40

from functools import partial
import math


def spam(a, b, c, d):
    '''
    可以看出 partial() 固定某些参数并返回一个新的 callable 对象。这个新的 callable
    接受未赋值的参数，然后跟之前已经赋值过的参数合并起来，最后将所有参数传递给
    原始函数
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    '''
    print(a, b, c, d)


points = [(1, 2), (3, 4), (5, 6)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


def output_result(result, log=None):
    if log is not None:
        log.debug('Got: {!r}'.format(result))


def add(x, y):
    return x + y


if __name__ == '__main__':
    spam(1, 2, 3, 4)
    s1 = partial(spam, 1)
    print(s1(2, 3, 4), s1(4, 5, 6))
    s2 = partial(spam, d=42)
    print(s2(1, 2, 3))
    s3 = partial(spam, 1, 2, d=4)
    print(s3(3), s3(5))
    pt = (4, 3)
    points.sort(key=partial(distance, pt))
    print(points)
    import logging
    from multiprocessing import Pool

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()
