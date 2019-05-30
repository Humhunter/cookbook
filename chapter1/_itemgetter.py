#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/30 8:48

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


def sort_dict():
    rows_by_name = sorted(rows, key=itemgetter('fname'))
    rows_by_id = sorted(rows, key=itemgetter('uid'))
    rows_by_flname = sorted(rows, key=itemgetter('fname', 'lname'))
    print(rows_by_name)
    print(rows_by_id)
    print(rows_by_flname)
    rows_by_lfname = sorted(rows, key=lambda k: (k['lname'], k['fname']))
    print(rows_by_lfname)


def max_min_dict():
    max_dict = max(rows, key=itemgetter('uid'))
    min_dict = min(rows, key=itemgetter('uid'))
    print(max_dict, min_dict)


if __name__ == '__main__':
    sort_dict()
