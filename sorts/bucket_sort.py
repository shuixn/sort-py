#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bucket sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from .base import *
from typing import List
from .quick_sort import QuickSort
import copy

class BucketSort(Base):
    length = 10
    process = []

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        bucket_length = max(L) // 10 + 1
        buckets = [[] for i in range(0, bucket_length)]
        for i in L:
            buckets[i // 10].append(i)

        for i in buckets:
            quicksort = QuickSort(len(i))
            i = quicksort.execute(i)

        sort_L = []
        for i in buckets:
            if isinstance(i, list):
                for j in i:
                    sort_L.append(j)
            else:
                sort_L.append(i)

        return sort_L