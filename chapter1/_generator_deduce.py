#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/31 9:26

from os import listdir

aList = [6, 2, -3, 5, -4, 8]


def what_generator_deduce():
    '''
    列表推导式和生成器表达式结构一样,但是生成器表达式是惰性计算，也就是每次只处理一个对象
    '''
    deduce1 = [x for x in aList if x > 0]
    generator1 = (x for x in aList if x > 0)
    print(deduce1, type(deduce1))
    print(generator1, type(generator1))


files = listdir(r'C:\Users\qidian\PycharmProjects\workplace\cookbook')
if any(name.endswith('.py') for name in files):
    print('there be python!')
else:
    print('Sorry, no python')

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
min_shares_key = min(portfolio, key=lambda k: k['shares'])
print(min_shares_key)

if __name__ == '__main__':
    what_generator_deduce()
