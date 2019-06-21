#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/6/21 8:29


from datetime import timedelta
from datetime import datetime


def main():
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    print(a, b)
    now = datetime.today()
    print(now, now.weekday())
    print(now + timedelta(hours=2))
    print(now - timedelta(days=1))
    print(now + timedelta(days=1))


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_data=None):
    if start_data is None:
        start_data = datetime.today()
    day_num = start_data.weekday()
    day_num_target = weekdays.index(dayname)


if __name__ == '__main__':
    main()
