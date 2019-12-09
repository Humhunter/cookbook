#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/12/9 20:45


from functools import wraps


def get_message(message):
    print('Got a message: {}'.format(message))


def root_call(func, message):
    print(func(message))


def func_example(message):
    def get_message_1(message):
        print('Got a message_1: {}'.format(message))

    return get_message_1(message)


def func_closure():
    def get_message_2(message):
        print('Got a message_2: {}'.format(message))

    return get_message_2


def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


def greet():
    print('hello world')


def my_decorator_1(func):
    @wraps(func)
    def wrapper(message):
        print('wrapper of decorator')
        func(message)

    return wrapper


@my_decorator_1
def greet_decorator(message):
    print(message)


def repeat(num):
    def my_decoretor_define(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decoretor_define


@repeat(5)
def greet_repeat(message):
    print(message)


# study the decorator of class
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('number of calls is : {}'.format(self.num_calls))
        return self.func(*args, **kwargs)


@Count
def example():
    print('hello world')


def main():
    root_call(get_message, 'Hello World')
    func_example('hello world')
    send_message = func_closure()
    send_message('hello world')


if __name__ == '__main__':
    main()
    print('=========================')
    greet = my_decorator(greet)
    greet()
    print('=========================')
    greet_decorator('hello world 3 thousand')
    print('=========================')
    greet_repeat('I am the best')
    print('=========================')
    example()
    example()