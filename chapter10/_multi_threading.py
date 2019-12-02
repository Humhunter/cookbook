#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/11/15 17:24


import time, threading


def loop():
    print('thread {} is running'.format(threading.current_thread().name))
    n = 0
    while n < 5:
        n = n + 1
        print('thread {0} >>>> {1}'.format(threading.current_thread().name, n))
        time.sleep(1)
    print('thread {} ended'.format(threading.current_thread().name))


balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


if __name__ == '__main__':
    print('thread {} is running'.format(threading.current_thread().name))
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread {} ended.'.format(threading.current_thread().name))
    print('---------我是分隔符--------------')
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
