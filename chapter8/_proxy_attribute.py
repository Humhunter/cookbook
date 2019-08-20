#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/8/9 19:23


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:
    """
    简单的代理
    """
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass


class B2:
    '''
    使用 __getattr__ 的代理，代理方法比较多时候
    '''
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, name):
        '''
        这个方法在访问的 attribute 不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found
        :param name:
        :return:
        '''
        print('Calling __getattr__')
        return getattr(self._a, name)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        print('Getting: ', item)
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('Settting: ', key, value)
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('Deletting: ', item)
            delattr(self._obj, item)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


if __name__ == '__main__':
    b = B2()
    print(b.bar())
    print(b.spam(42))
    # 使用这个代理类时， 你只需要用他来包装下其他类即可
    s = Spam(2)
    p = Proxy(s)
    print(p.x)
    print(p.bar(3))
    print(p.x)
