#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/15 17:28


def define_lambda():
    # 匿名函数是在运行时绑定值，而不是定义时就绑定
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y
    print(a(10), b(10))
    # 如果你想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10), b(10))


def lambda_example():
    funcs = [lambda x: x + n for n in range(5)]
    for f in funcs:
        print(f(0))
    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print(f(0))


if __name__ == '__main__':
    define_lambda()
    lambda_example()
