#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/8/5 12:42


from abc import ABCMeta, abstractmethod
import io
import collections


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


if __name__ == '__main__':
    # 抽象类的一个特点是它不能直接被实例化
    try:
        a = IStream()
    except TypeError as e:
        print(e)


    # 抽象类的目的就是让别的类继承它并实现特定的抽象方法
    class SocketStream(IStream):
        def read(self, maxbytes=-1):
            pass

        def write(self, data):
            pass


    # 抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口
    def serialize(obj, stream):
        if not isinstance(stream, IStream):
            raise TypeError('Expected an IStream')
        pass


    # 除了继承方式外，还可以通过注册方式来实现让某个类实现抽象基类
    IStream.register(io.IOBase)

    f = open('foo.txt')
    isinstance(f, IStream)
