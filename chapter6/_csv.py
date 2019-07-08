#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/1 18:32


import csv
from collections import namedtuple


def csv_example():
    with open('stocks.csv', 'rt') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            print(row)

    with open('stocks.csv', 'rt') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            print(row, type(row))

    with open('stocks.csv', 'rt') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row, type(row))


def csv_write():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [
        ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
    ]
    with open('stocks.csv', 'wt', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def csv_convert():
    col_types = [str, float, str, str, float, int]
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)

    print('Reading as dicts with type conversion')


if __name__ == '__main__':
    csv_example()
    csv_write()
