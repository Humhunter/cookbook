#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/1 18:13


import pickle
import threading
import time


def pickle_example():
    f = open('somedata', 'wb')
    pickle.dump([1, 2, 3, 4], f)
    pickle.dump('hellowolrd', f)
    pickle.dump({'apple', 'pear', 'banana'}, f)
    f.close()
    f = open('somedata', 'rb')
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))


class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


if __name__ == '__main__':
    pickle_example()
    c = Countdown(30)
    f = open('cstate.p', 'wb')
    pickle.dump(c, f)
    f.close()
    f = open('cstate.p', 'rb')
    pickle.load(f)
    f.close()