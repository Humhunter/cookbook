#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/24 8:23

import linecache


def file_open():
    '''
    1. read() 方法用来直接读取字节到字符串中, 最多读取给定数目个字节. 如果没有给定 size 参数(默认值为 -1)或者 size 值为负,
    文件将被读取直至末尾. 未来的某个版本可能会删除此方法.

    2. readline() 方法读取打开文件的一行(读取下个行结束符之前的所有字节). 然后整行，包括行结束符，作为字符串返回. 和 read()
    相同, 它也有一个可选的 size 参数, 默认为 -1, 代表读至行结束符. 如果提供了该参数, 那么在超过 size 个字节后会返回不完整的行.

    3. readlines() 方法并不像其它两个输入方法一样返回一个字符串. 它会读取所有(剩余的)行然后把它们作为一个字符串列表返回. 它的
    可选参数 sizhint 代表返回的最大字节大小. 如果它大于 0 , 那么返回的所有行应该大约有 sizhint 字节(可能稍微大于这个数字, 因为需要凑齐缓冲区大小).

    4. linecache 有特殊需求还可以用linecache模块，比如你要输出某个文件的第n行：
    :return:
    '''
    with open('somefile1.txt', 'r') as f:
        print(f.readlines())

    text = linecache.getline('somefile1.txt', 2)
    print(text)

    with open('somefile1.txt', 'at') as f:
        print('I AM THE FIRST', file=f)


def print_sep():
    for i in range(5):
        print(i, end=' ')
    row = ('ACME', 50, 91.5)
    print(*row, sep=',')
    print(','.join(str(x) for x in row))  # 如果用join，会导致类型不相符,只能 print(','.join(str(x) for x in row))


if __name__ == '__main__':
    file_open()
    print_sep()
    try:
        with open('somefile1.txt', 'xt') as f:
            print(f.read())
    except Exception as e:
        print(e)
