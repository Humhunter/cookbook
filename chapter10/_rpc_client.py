#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/11/13 15:59


import pickle


class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result

        return do_rpc


if __name__ == '__main__':
    from multiprocessing.connection import Client

    c = Client(('localhost', 17000), authkey=b'humhunter')
    proxy = RPCProxy(c)
    print(proxy.add(2, 3))
