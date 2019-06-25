#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/25 22:49


import os
import sys
import time


def os_common():
    path = 'E:\Pycharmprojectfile\cookbook'
    print(os.path.basename(path), os.path.dirname(path))
    print(os.path.join('tmp', 'data', os.path.basename(path)))
    path = '~/Data/data.csv'
    # Expand the user's home directory
    print(os.path.expanduser(path))
    print(os.path.splitext(path))


def os_judge():
    print(os.path.exists('/etc/passwd'))
    print(os.path.isfile('/etc/passwd'))
    # Is a symbolic link
    print(os.path.islink('/etc/passwd'))
    # Get the file linked to
    os.path.realpath('/usr/local/bin/python3')
    print(os.path.isdir('/etc/passwd'))


def os_size():
    filepath = '../chapter4/somefile1.txt'
    print(os.path.getsize(filepath))
    print(os.path.getmtime(filepath), os.path.getatime(filepath), os.path.getctime(filepath))
    print(time.ctime(os.path.getmtime(filepath)))


def os_list():
    path = 'E:\Pycharmprojectfile\cookbook'
    names = os.listdir(path)
    print(names)
    filenames = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    print(filenames)
    dirnames = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    print(dirnames)


def glob_fnmatch():
    import glob
    from fnmatch import fnmatch
    path = 'E:\Pycharmprojectfile\cookbook'
    pyfiles = glob.glob(os.path.join(path, '*.py'))
    print(pyfiles)
    pyfiles = [name for name in os.listdir(path) if fnmatch(name, "*.py")]
    print(pyfiles)


def get_file_information():
    import glob
    pyfiles = glob.glob('*.py')
    name_sz_data = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]
    for name, size, mtime in name_sz_data:
        print(name, size, time.ctime(mtime))
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, stat in file_metadata:
        print(name, stat)


def os_encoding():
    print(sys.getfilesystemencoding())


if __name__ == '__main__':
    os_common()
    os_judge()
    os_size()
    os_list()
    glob_fnmatch()
    get_file_information()
    os_encoding()