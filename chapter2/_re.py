#! /usr/bin/env python
# -*- coding: utf-8 -*-
# auther : xiaojinsong(61627515@qq.com)


import re


def re_split():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    result = re.split(r'[;,\s]\s*', line)
    fields = re.split(r'(;|,|\s)\s*', line)  # 带有括号捕获分组,就是说分隔符也会在结果列表中
    print(result)
    print(fields)


def re_compile():
    pattern = re.compile(r'o')
    print(pattern.match('dog'))
    print(re.match(r'o', 'dog'))  # 和上面等价
    print(pattern.search('dog'))
    print(re.search(r'o', 'dog'))  # 和上面等价


def re_findall():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.findall(text))
    m = datepat.match('06/03/2019')
    print(m.group(0), m.group(1), m.group(2), m.group(3), m.groups(), type(m.groups()))


def re_sub():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(r'\3-\1-\2', text))  # 反斜杠数字比如 \3 指向前面模式的捕获组号
    newtext, n = datepat.subn(r'\3-\1-\2', text)
    print(newtext, n)


if __name__ == '__main__':
    re_split()
    re_compile()
    re_findall()
    re_sub()
