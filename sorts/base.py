#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""base utils"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

import random
import time
from typing import List
from functools import partial

class CaculateTime:
    _func = None

    def __init__(self, func):
        self._func = func

    def __get__(self, obj, cls):
        return partial(self.__call__, obj)

    def __call__(self, *a, **kw):
        start = time.time()
        result = self._func(*a, **kw)
        print("consume time: {1}".format(self._func.__name__, time.time() - start))
        return result

class Base:
    length = 0

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        return L

    def generator(self) -> List[int]:
        l = list(range(self.length))
        random.shuffle(l)
        return l

    def print_list(self, title: str, list: List[int]) -> None:
        print(title + ', ' . join('%s' % id for id in list))

    def main(self, length: int = 10):
        self.length = length
        list = self.generator()
        self.print_list('nums: ', list)
        list = self.execute(list)
        self.print_list('after sorted: ', list)