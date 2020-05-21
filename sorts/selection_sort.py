#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""selection sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from .base import *
from typing import List
import copy

class SelectionSort(Base):
    length = 10
    process = []

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        self.process.append(copy.deepcopy(L))
        for i in range(self.length):
            min_index = i
            for j in range(i + 1, self.length):
                if L[min_index] > L[j]:
                    min_index = j
            L[min_index], L[i] = L[i], L[min_index]
            self.process.append(copy.deepcopy(L))
        return L