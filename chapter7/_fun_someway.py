#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/10 8:50
import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


def make_element(name, value, **attrs):
    # keyvals = ['{items.key()}="{item.value()}"'.format(item for item in attrs.items()]
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element


def a_example(x, *args, y):
    pass


def b_example(x, *args, y, **kwargs):
    pass


def recv(maxsize, *, block):
    'Receives a message'
    pass


def minnum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


def add(x: int, y: int) -> int:
    '''
    给函数注解
    :param x:
    :param y:
    :return:
    '''
    return x + y


def myfun():
    return 1, 2, 3


_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


x = 42


def spam1(a, b=x):
    print(a, b)


if __name__ == '__main__':
    print(avg(1, 2))
    print(avg(1, 2, 3, 4, 5))
    print(make_element('item', 'Albatross', size='large', quantity=6))
    try:
        recv(1024, True)
    except Exception as e:
        print(e)
    recv(1024, block=True)
    a_min = minnum(1, 5, 2, -5, 10)
    b_min = minnum(1, 5, 2, -5, 10, clip=0)
    print(a_min)
    print(b_min)
    # 函数注解只存储在函数的 annotations 属性
    print(add.__annotations__)
    a, b, c = myfun()
    print(a, b, c, type(c))
    d = myfun()
    print(d, type(d))
    spam(1)
    print(spam(1, 2), spam(1, None))
    # 1、注意到当我们改变 x 的值的时候对默认参数值并没有影响，这是因为在函数定义的时候就已经确定了它的默认值了
    # 2、默认参数的值应该是不可变的对象，比如 None、True、False、数字或字符串
    print(spam1(1))
    x = 13
    print(spam1(1))
