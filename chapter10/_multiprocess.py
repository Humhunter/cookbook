#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/11/13 17:54


import os, time, random
from multiprocessing import Pool
import subprocess
from multiprocessing import Process, Queue


def run_proc(name):
    print('Run child process {} ({})'.format(name, os.getpid()))


def long_time_task(name):
    print('Run task {} ({})'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task {} run {:.2f} seconds'.format(name, (end - start)))


def write(q):
    print('Process to write {}'.format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put {} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read {}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('Get {} from queue...'.format(value))


if __name__ == '__main__':
    print('Parent process {}'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('Child process will start....')
    p.start()
    p.join()
    print('child process end..')
    print('--------我是分隔符----------')
    print('Parent process {}'.format(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done..')
    p.close()
    p.join()
    print('ALL subprocess done...')
    print('---------我是分隔符---------')
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output)
    print('Exit code:', p.returncode)
    print('---------我是分隔符---------')
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
