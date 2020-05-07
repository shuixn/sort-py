#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bubble sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from .base import *
from typing import List
import copy

class BubbleSort(Base):
    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        process = []
        process.append(copy.deepcopy(L))
        for i in range(0, self.length):
            for j in range(i + 1, self.length):
                if L[i] > L[j]:
                    L[i], L[j] = L[j], L[i]
                    process.append(copy.deepcopy(L))
        print(process)
        animate = Animate()
        animate.save(process, 'bubble_sort')
        return L