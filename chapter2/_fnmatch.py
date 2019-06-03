#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/3 8:45


from fnmatch import fnmatch, fnmatchcase


def common_match():
    filename = 'spam.txt'
    print(filename.startswith('file:'))
    print(filename.endswith('.txt'))
    # 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去
    filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    print([name for name in filenames if name.endswith(('.c', '.h'))])


def fnmatch_match():
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    # fnmatchcase 严格区分大小写
    print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
    print([addr for addr in addresses if fnmatchcase(addr, '* st')])


if __name__ == '__main__':
    common_match()
    fnmatch_match()