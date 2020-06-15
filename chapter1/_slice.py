#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/29 9:09


def slice_pre():
    # 1
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])
    print(int(record[20:23]), float(record[31:37]), cost)
    # 2
    shares = slice(20, 23)
    price = slice(31, 37)
    print(int(record[shares]) * float(record[price]))



def slice_indices():
    '''
    你还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序
    列上，这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以
    满足边界限制，从而使用的时候避免出现 IndexError 异常
    :return:
    '''
    a = slice(5, 50, 2)
    print(a.start, a.stop, a.step)
    s = 'HelloWorld'
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])


if __name__ == '__main__':
    slice_pre()
    slice_indices()
