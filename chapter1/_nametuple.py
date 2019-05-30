#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/30 18:49


from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber(addr='qidian@yujiahui.com', joined='2012-10-19')
print(sub.addr, sub.joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])