#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/15 19:12

from collections import deque


def search(lines, patterns, history=5):
    previous_lines = deque(maxlen=5)
    for li in lines:
        if patterns in li:
            yield  li, previous_lines
        previous_lines.append(li)


if __name__ == '__main__':
    