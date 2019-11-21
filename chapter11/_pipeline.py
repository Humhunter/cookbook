#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/11/21 22:55


import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
