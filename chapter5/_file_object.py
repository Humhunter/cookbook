#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/26 9:15


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_simple_display(self):
        return f'{self.name}({self.age})'

    def get_long_dispaly(self):
        return f'{self.name} is {self.age} years old.'

    def __format__(self, format_spec):
        if format_spec == 'long':
            return f'{self.name} is {self.age} years old.'
        elif format_spec == 'simple':
            return f'{self.name}({self.age})'
        else:
            raise ValueError('invalid format spec')


if __name__ == '__main__':
    qidian = Student('qidian', '18')
    print(qidian.get_simple_display())
    print(qidian.get_long_dispaly())
