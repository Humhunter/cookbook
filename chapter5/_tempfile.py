#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/1 9:05


from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory
from tempfile import mkstemp,gettempdir


def temporaryfile_use():
    '''
    支持跟open一样的内置函数，encodeing， errors等
    :return:
    '''
    with TemporaryFile('w+t') as f:
        f.write('Hello World\n')
        f.write('Testing\n')
        f.seek(0)
        data = f.read()
    return data

def namedtemporaryfile_use():
    mkstemp()
    testtemp = gettempdir()
    print(testtemp)
    f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
    print(f.name)
    f.close()