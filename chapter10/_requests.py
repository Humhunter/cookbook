#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/11/13 11:23


import requests

r = requests.get('http://httpbin.org/get?name=Dave&age=37', headers={'User-agent': 'goaway/1.0'})
resp = r.json()
print(resp['headers'])
print(resp['args'])
