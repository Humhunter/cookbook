#! /usr/bin/env python
# -*- coding: utf-8 -*-
# auther : xiaojinsong(61627515@qq.com)


def manual_iter():
    with open('/etc/passwd', 'r') as f:
        try:
            while True