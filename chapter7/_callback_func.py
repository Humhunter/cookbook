#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/16 8:58


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print('Got: {}'.format(result))


def add(x, y):
    return x + y


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


def make_handler_coroutine():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


from queue import Queue
from functools import wraps


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('Hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('GoodBye')


def main():
    apply_async(add, (2, 3), callback=print_result)
    apply_async(add, ('Hello', 'Python'), callback=print_result)
    r = ResultHandler()
    # 1、为了让回调函数访问外部信息, 一种方法是使用一个绑定方法来代替一个简单函数
    apply_async(add, (3, 4), callback=r.handler)

    # 2、作为类的替代，可以使用一个闭包捕获状态值
    handler = make_handler()
    apply_async(add, (2, 5), callback=handler)

    # 3、使用协程来完成
    handler_coroutine = make_handler_coroutine()
    next(handler_coroutine)
    apply_async(add, (2, 8), callback=handler_coroutine.send)

    # 计算的暂停与重启思路跟生成器函数的执行模型不谋而合
    test()


if __name__ == '__main__':
    main()
