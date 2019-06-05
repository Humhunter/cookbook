#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/4 8:49


import unicodedata
import sys


def unicode_normalize():
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print(s1, len(s1), s2, len(s2))
    print(s1 == s2)
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print(t1 == t2)
    print(t1, ascii(t1), t2, ascii(t2))


def unicode_translate():
    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None  # Deleted
    }
    s = 'pýtĥöñ\fis\tawesome\r\n'
    a = s.translate(remap)
    print(a)
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    b = unicodedata.normalize('NFD', a)
    print(b)
    print(b.translate(cmb_chrs))


if __name__ == '__main__':
    unicode_normalize()
    unicode_translate()
