#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/20 19:48


from heapq import merge


def sort_multi_list():
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for i in merge(a, b):
        print(i)


def merge_file():
    with open('somefile1.txt', 'rt') as file1, open('somefile2.txt', 'rt') as file2, open('merge_file', 'wt') as outf:
        for line in merge(file1, file2):
            outf.write(line)


if __name__ == '__main__':
    sort_multi_list()
    merge_file()