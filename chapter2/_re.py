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


if __name__ == '__main__':
    re_split()
    re_compile()
