#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/8/20 19:21


import weakref


class Node:
    def __int__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_chlid(self, child):
        self.children.append(child)
        child.parent = self


if __name__ == '__main__':
    root = Node('parent')
    c1 = Node('chlid')
    root.add_chlid(c1)
    print(c1.parent)
