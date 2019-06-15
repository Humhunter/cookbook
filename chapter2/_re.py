#! /usr/bin/env python
# -*- coding: utf-8 -*-
# auther : xiaojinsong(61627515@qq.com)


import re
from collections import namedtuple

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


def match_case(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


def re_flag():
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print(re.findall('python', text, flags=re.IGNORECASE))
    print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
    print(re.sub('python', match_case('snake'), text, flags=re.IGNORECASE))


def re_greed():
    str_pattern = re.compile(r'"(.*)"')
    text1 = 'Computer says "no."'
    print(str_pattern.findall(text1))
    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pattern.findall(text2))  # 默认是贪婪模式，尽可能多的匹配
    str_pat = re.compile(r'"(.*?)"')
    print(str_pat.findall(text2))


def re_multiline():
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''
        /* this is a
         multiline comment */
    '''
    print(comment.findall(text1))
    print(comment.findall(text2))
    comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
    print(comment1.findall(text2))
    comment2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    print(comment2.findall(text2))


def re_token():
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'
    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
    scanner = master_pat.scanner('foo=42')
    print(scanner.match())
    print(scanner.match().lastgroup, scanner.match().group())

def generate_token():
    Token = namedtuple('Token', ['type', 'value'])


if __name__ == '__main__':
    re_split()
    re_compile()
    re_findall()
    re_sub()
    re_flag()
    re_greed()
    re_multiline()
    re_token()
    generate_token()