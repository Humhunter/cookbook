#!/usr/bin/env python
#  -*- coding: utf-8 -*-
#  @Time    : 2019/10/3 9:15 PM
#  @Author  : Jingsong.xiao
#  @Email   : fly.xiaojs@gmail.com


from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        # @wraps(func)
        # def wrapper(*args, **kwargs):
        #     bound_types =