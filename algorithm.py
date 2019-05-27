#! /usr/bin/env python
# -*- coding: utf-8 -*-
# auther : xiaojinsong(61627515@qq.com)


# 插入排序
def insert_sort(aList):
    '''
    1、从第一个元素开始，该元素可以认为已经被排序
    2、取出下一个元素，在已经排序的元素序列中从后向前扫描
    3、如果该元素（已排序）大于新元素，将该元素移到下一位置
    4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    5、将新元素插入到该位置中
    6、重复步骤2
    :param aList:
    :return:
    '''
    count = len(aList)
    for i in range(1, count):
        key = aList[i]
        j = i - 1
        while j >= 0:
            if aList[j] > key:
                aList[j + 1] = aList[j]
                aList[j] = key
            j -= 1
    return aList

aList = [28, 32, 14, 12, 53, 42]
print(insert_sort(aList))


# 冒泡排序
def bubble_sort(aList):
    '''
    1、比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    3、针对对所有的元素重复以上的步骤，除了最后一个。
    4、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
    :param aList:
    :return:
    '''
    count = len(aList)
    for i in range(0, count - 1):
        for j in range(0, count - i - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]


aList = [28, 32, 14, 12, 53, 42]

# 快速排序
def quick_sort(aList, start, end):
    if start >= end:
        return