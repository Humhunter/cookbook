#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/30 18:34


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Settting name to {}'.format(value))
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPerseon1(Person):
    @Person.name.getter
    def name(self):
        print("Getting name")
        return super().name


class SubPerson2(Person):
    @Person.name.setter
    def name(self):
        print("")


if __name__ == '__main__':
    s = SubPerson('Jinsong')
    print(s.name)
    s.name = 'qidian'
    print(s.name)
    try:
        s.name = 31
    except TypeError as e:
        print(e)
