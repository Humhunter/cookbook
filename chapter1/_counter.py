#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/5/29 18:42


from collections import Counter


def counter_element():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]

    word_counts = Counter(words)
    #  Counter 对象可以接受任意的 hashable 序列对象。在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上
    print(word_counts['eyes'], word_counts['look'])
    top_three = word_counts.most_common(3)
    print(top_three)


def counter_calculate(method):
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_counts = Counter(words)
    # 1
    if method == 1:
        for word in morewords:
            word_counts[word] += 1
        print(word_counts['eyes'], word_counts['look'])
    # 2
    elif method == 2:
        word_counts.update(morewords)
        print(word_counts['eyes'], word_counts['look'])
    #
    else:
        a = Counter(words)
        b = Counter(morewords)
        c = a + b
        d = a - b
        print(c, d)


if __name__ == '__main__':
    counter_element()
    counter_calculate(1)
    counter_calculate(2)
    counter_calculate(3)