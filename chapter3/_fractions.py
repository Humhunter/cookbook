#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/13 8:18


from fractions import Fraction


if __name__ == '__main__':
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    c = a * b
    print(a, b, a+b, c, c.numerator, c.denominator)
