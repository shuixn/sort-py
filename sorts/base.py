#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""base utils"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

import random
import time
from typing import List
from functools import partial
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt

class CaculateTime:
    _func = None

    def __init__(self, func):
        self._func = func

    def __get__(self, obj, cls):
        return partial(self.__call__, obj)

    def __call__(self, *a, **kw):
        start = time.time()
        result = self._func(*a, **kw)
        print("consume time: {0}".format(time.time() - start))
        return result

class Base:
    length = 0
    process = []

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        return L

    def generator(self) -> List[int]:
        l = list(range(1, self.length + 1))
        random.shuffle(l)
        return l

    def print_list(self, title: str, list: List[int]) -> None:
        print(title + ', ' . join('%s' % id for id in list))

    def save_animate(self):
        animate = Animate()
        animate.save(self.process, self.__class__.__name__)

    def main(self, length: int = 10):
        self.length = length
        list = self.generator()
        self.print_list('nums: ', list)
        list = self.execute(list)
        self.print_list('after sorted: ', list)

class Animate:
    def animate(self, i):
        for rect, yi in zip(self.rects, self.data[i]):
            rect.set_color('b')
            rect.set_height(yi)
            
            # x = [i for i in range(len(self.data[0]))]
            # for a,b in zip(x, self.data[i]):
            #     plt.text(a, b+0.05, b, ha='center', va= 'bottom',fontsize=11)

            diff_nums = self.get_diff_nums(i)
            if diff_nums:
                if yi in diff_nums:
                    rect.set_color("g")
        return self.rects

    def get_diff_nums(self, i):
        if i == len(self.data) - 1:
            return None
        nums = []
        for i_index, i_item in enumerate(self.data[i]):
            if self.data[i+1][i_index] != i_item:
                nums.append(i_item)
        return nums

    def save(self, data: List[int], filename: str):
        self.data = data

        fig = plt.figure(figsize=(8, 4))
        x = [i for i in range(len(self.data[0]))]

        self.rects = plt.bar(x, self.data[0])
        plt.ylim(0, len(self.data[0]))

        anim = animation.FuncAnimation(fig, self.animate, frames=len(self.data), interval=1000)
        anim.save('gifs/%s.gif' % filename, writer='pillow')