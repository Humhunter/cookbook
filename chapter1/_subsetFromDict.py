#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/30 18:44


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

if __name__ == '__main__':
    p1 = {key: value for key, value in prices.items() if value > 200}
    teach_names = ['AAPL', 'FB']
    p2 = {key: value for key, value in prices.items() if key in teach_names}
    p3 = dict((key, value) for key, value in prices.items() if value > 200)
    print(p1, p2, p3)