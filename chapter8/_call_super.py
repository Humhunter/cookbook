#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/30 17:32


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


class C:
    def __init__(self):
        self.x = 0


class D(C):
    def __init__(self):
        super().__init__()
        self.y = 1


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


class Base:
    def __init__(self):
        print('Base.__init__')


class E(Base):
    def __init__(self):
        super().__init__()
        print('E.__init__')


class F(Base):
    def __init__(self):
        super().__init__()
        print('F.__init__')


class G(E, F):
    def __init__(self):
        super().__init__()
        print('G.__init__')


if __name__ == '__main__':
    # a = A()
    b = B()
    print(b.spam())
    c = C()
    d = D()
    print(d.x, d.y)
    g = G()
    # Python 会计算出一个所谓的方法解析顺序 (MRO) 列表。这个 MRO 列表就是一个简单的所有基类的线性顺序表
    print(g, G.__mro__)