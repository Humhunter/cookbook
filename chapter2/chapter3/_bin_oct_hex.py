#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/11 8:19


if __name__ == '__main__':
    x = 1234
    print(bin(x))
    print(oct(x))
    print(hex(x))

    '''
    如果你不想使用0b,0o,0x这类前缀的话，可以使用format函数
    '''
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    x = -1234
    print(format(x, 'b'))
    print(format(x, 'x'))

    '''
    如果你想产生一个无符号值，你需要增加一个指示最大位长度的值，比如为了显示32位的值
    '''

    x = -1234
    print(format(2**32 + x, 'b'))
    print(format(2**32 + x, 'x'))

    '''
    为了以不同的进制转换整数字符串，简单的使用带有进制的 int() 函数即可
    '''
    print(int('4d2', 16))
    print(int('10011011010', 2))