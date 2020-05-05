#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""base util"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

import random
from typing import List

class Base:
    length = 0

    def execute(self, L: List[int]) -> List[int]:
        return L

    def generator(self) -> List[int]:
        l = list(range(self.length))
        random.shuffle(l)
        return l

    def main(self, length: int = 10):
        self.length = length
        list = self.generator()
        print('nums: ' + ', ' . join('%s' % id for id in list))
        list = self.execute(list)
        print('after sorted: ' + ', ' . join('%s' % id for id in list))