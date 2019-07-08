#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/7/4 8:41

from collections import OrderedDict
from pprint import pprint
import json
import requests

data = {
    'name': 'ACE',
    'shares': 100,
    'price': 542.23,
}

s = '{"name": "ACME", "shares": 50, "price": 490.1}'


def json_example():
    global data
    json_str = json.dumps(data)
    print(json_str, type(json_str))
    data = json.loads(json_str)
    with open('data.json', 'w') as f:
        json.dump(data, f)
    with open('data.json', 'r') as f:
        data = json.load(f)


def pprint_example():
    # u = urlopen('https://yandex.com/search/?text=python&lr=20895')
    paras = {
        'text': 'python',
        'lr': 20895
    }
    r = requests.get('https://yandex.com/search/', params=paras)
    print(r.text)
    # resp = json.loads(u.read().decode('utf-8'))
    # pprint(resp)


def json_objects_pairs_hook():
    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)


class JsonObject:
    def __init__(self, d):
        self.__dict__ = d


def json_objects_hook():
    data = json.loads(s, object_hook=JsonObject)
    print(data.name, data.shares, data.price)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d


if __name__ == '__main__':
    json_example()
    pprint_example()
    json_objects_pairs_hook()
    json_objects_hook()
    p = Point(3, 4)
    try:
        json.dumps(p)
    except Exception as e:
        print(e)
    finally:
        print('Just for test')
    s = json.dumps(p, default=serialize_instance)
    print(s)
