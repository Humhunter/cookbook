#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/26 15:17


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        '''
        A public method
        :return:
        '''
        pass

    def _internal_method(self):
        pass


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()


class C(B):
    # 你定义的一个变量和某个保留关键字冲突，这时候可以使用单下划线作为后缀
    lambda_ = 2.0

    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        pass


if __name__ == '__main__':
    '''
    大多数而言，你应该让你的非公共名称以单下划线开
    头。但是，如果你清楚你的代码会涉及到子类，并且有些内部属性应该在子类中隐藏
    起来，那么才考虑使用双下划线方案
    '''
    b = B()
    # print(B.__private)
