#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/10 8:31


from datetime import datetime, timedelta
import time
import calendar


def print_datetime():
    print(datetime.now(), datetime.today(), datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.today().date(),
          sep='\n')
    now = datetime.now()
    print(now)
    print(now + timedelta(hours=10))
    print(now + timedelta(days=1))
    print(now - timedelta(days=1))


def print_time():
    pass


def print_calender():
    pass


if __name__ == '__main__':
    print_datetime()
    print_time()
