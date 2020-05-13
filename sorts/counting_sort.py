#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""counting sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from .base import *
from typing import List
import copy

class CountingSort(Base):
    length = 10
    process = []

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        n = len(L)
        max_value = max(L)
        min_value = min(L)
        count=[0] * (max_value - min_value + 2)
        for i in range(0, n):
            count[L[i]] += 1

        sort_L = []
        for i in range(0, max_value + 1):
            for j in range(0, count[i]):
                sort_L.append(i)
        return sort_L