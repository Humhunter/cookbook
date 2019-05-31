#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/30 18:49


from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber(addr='qidian', joined='2012-10-19')
sub1 = Subscriber('yuanma', '2015-03-08')
print(sub.addr, sub.joined)
print(sub1.addr, sub1.joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
records = [
    ['girl1', 5, 200],
    ['girl2', 10, 300],
    ['girl3', 15, 500],
]


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


Stock1 = namedtuple('Stock1', ['name', 'shares', 'price', 'date', 'time'])
stock1_prototype = Stock1('', 0, 0.0, None, None)


def dict_to_stock(s):
    '''
    因为是命名元祖，所以是不能直接修改值，依赖_replace()方法,它会创建一个全新的命名元组并将对应的字段用新的值取代
    :param s:
    :return:
    '''
    return stock1_prototype._replace(**s)


if __name__ == '__main__':
    result = compute_cost(records)
    print(result)
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(dict_to_stock(a))
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(b))