#! /usr/bin/env python
# -*- coding: utf-8 -*-
# auther : xiaojinsong(61627515@qq.com)


parts = ['Is', 'Chicago', 'Not', 'Chicago?']
data = ['ACME', 50, 91.1]
print(' '.join(parts))


def generate_str():
    print(','.join(str(d) for d in data))


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts=[]
            size = 0
        yield ''.join(parts)


if __name__ == '__main__':
    generate_str()
    text = ','.join(sample())
    print(text)
    with open('combine.txt', 'w') as f:
        for part in combine(sample(), 32768):
            f.write(part)