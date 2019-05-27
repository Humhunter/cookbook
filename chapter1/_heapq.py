#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/22 8:33


import heapq
import numpy as np


def nlargest_and_nsmallest():
    nums = list([np.random.randint(20, size=10)])
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))


def nlargest_and_nsmallest_dict():
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    print('最便宜的三个为{!r}'.format(cheap))
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print('最贵的三个为{!r}'.format(expensive))


def list_to_heap():
    # list to heap
    '''
     把列表转为堆，堆数据结构最重要的特征是 heap[0] 永远是最小的元素。并且剩余的元素可以很
     容易的通过调用 heapq.heappop() 方法得到，该方法会先将第一个元素弹出来，然后
     用下一个最小的元素来取代被弹出元素 (这种操作时间复杂度仅仅是 O(log N)
     '''
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heapq.heapify(nums)
    print(nums)
    heapq.heappop(nums)
    print(nums)
    heapq.heappop(nums)
    print(nums)
    heapq.heappop(nums)
    print(nums)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def printheap(self):
        print(self._queue)


#
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)



if __name__ == '__main__':
    nlargest_and_nsmallest()
    nlargest_and_nsmallest_dict()
    list_to_heap()

    # 优先级队列
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('qidian'), 30)
    q.push(Item('yuanma'), 26)
    q.push(Item('qiaomai'), 35)
    q.printheap()
    print(q.pop())
    print(q.pop())