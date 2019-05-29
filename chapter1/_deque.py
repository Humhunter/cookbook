#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/15 19:12
'''
保留最后N个元素

'''

from collections import deque


def search(lines, patterns, history=5):
    previous_lines = deque(maxlen=5)
    for li in lines:
        if patterns in li:
            yield li, previous_lines
        previous_lines.append(li)


def get_last_num_element(n):
    q = deque(maxlen=n)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.append(4)
    q.append(5)
    print(q)


def deque_pop():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.appendleft(4)
    print(q)
    q.pop()
    print(q)
    q.popleft()
    print(q)


if __name__ == '__main__':
    get_last_num_element(3)
    deque_pop()
    with open('somefile.txt', 'r') as f:
        for line, prevlines in search(f, 'no', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 30)
