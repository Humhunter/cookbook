#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/8/8 18:47


import collections
import bisect


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._item = sorted(initial) if initial is not None else []

    # Required sequece methods
    def __getitem__(self, index):
        return self._item[index]

    def __len__(self):
        return len(self._item)

    def add(self, other):
        bisect.insort(self._item, other)


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    #Required sequence methods
    def __getitem__(self, index):
        print('Getting: ', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting: ', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Inserting: ', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting: ', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('len')
        return len(self._items)


if __name__ == '__main__':
    items = SortedItems([5, -1, 3])
    print(list(items))
    print(items[0], items[-1])
    items.add(2)
    print(list(items))
    items = SortedItems()
    import collections
    print(isinstance(items, collections.Iterable))
    print(isinstance(items, collections.Sequence))
    print(isinstance(items, collections.Container))
    print(isinstance(items, collections.Sized))
    print(isinstance(items, collections.Mapping))

    a = Items([1,2,3])
    print(len(a))
    print(a.append(4))
    print(a.append(2))
    print(a.count(2))
    print(a.remove(3))
