#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/16 8:41


from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


yandex = UrlTemplate('https://yandex.com/search/?{text}&{lr}')
for line in yandex.open(text='peace', lr='aqs=20895'):
    print(line.decode('utf-8'))


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


yandex = urltemplate('https://yandex.com/search/?{text}&{lr}')
for line in yandex(text='peace', lr='aqs=20895'):
    print(line.decode('utf-8'))
