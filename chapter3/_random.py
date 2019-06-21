#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/21 8:02


import random


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6,]
    alist = ['yes', 'y', 'no', 'n']
    print(random.choice(values))
    print(random.choice(alist))
    print(random.sample(values, 2))
    print(random.shuffle(values), values)
    print(random.randint(1, 10))