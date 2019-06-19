#! /usr/bin/env python
# -*- coding: utf-8 -*-
# auther : xiaojinsong(61627515@qq.com)
from collections import deque


def manual_iter():
    with open('passwd.txt', 'r') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


class TreeNode:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


class LineStory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


def iter_islice():
    '''
    一个需要注意的小地方是，如果你在迭代操作时不使用 for 循环语句，那么你得先
    调用 iter() 函数
    '''
    c = Countdown(30)
    import itertools

    for x in itertools.islice(c, 10, 20):
        print(x)

    for x in itertools.islice(c, 10, None):
        print(x)

    for x in itertools.islice(c, None, 10):
        print(x)


def iter_dropwhile():
    from itertools import dropwhile
    with open('passwd.txt') as f:
        while True:
            line = next(f, '')
            if not line.startswith('#'):
                break

        while line:
            print(line, end='')
            line = next(f, None)

    with open('passwd.txt') as f:
        lines = (line for line in f if not line.startswith('#'))
        for line in lines:
            print(line)

    with open('passwd.txt', 'r') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')


if __name__ == '__main__':
    manual_iter()
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    for ch in root:
        print(ch)
    root = TreeNode(0)
    child1 = TreeNode(1)
    child2 = TreeNode(2)
    root.add_children(child1)
    root.add_children(child2)
    child1.add_children(TreeNode(3))
    child1.add_children(TreeNode(4))
    child2.add_children(TreeNode(5))
    for ch in root.depth_first():
        print(ch)
    for rr in reversed(Countdown(30)):
        print(rr)
    for rr in Countdown(30):
        print(rr)
    with open('passwd.txt', 'r') as f:
        lines = LineStory(f)
        for line in lines:
            if 'kafka' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')
    iter_islice()
    for i in range(10):
        print(i)
    iter_dropwhile()
