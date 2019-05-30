#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/30 12:29

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(31), User(26)]
    print(users)
    print(sorted(users, key=attrgetter('user_id')))
    print(sorted(users, key=lambda u: u.user_id))


if __name__ == '__main__':
    sort_notcompare()
