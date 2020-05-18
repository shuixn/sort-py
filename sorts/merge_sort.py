#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from .base import *
from typing import List
import copy

class MergeSort(Base):
    length = 10
    process = []

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:        
        return self.merge_sort(L)

    def merge(self, a: List[int], b: List[int]) -> List[int]:
        merged = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged

    def merge_sort(self, L: List[int]) -> List[int]:
        if len(L) <= 1:
            return L
        mid = len(L) // 2
        a = self.merge_sort(L[:mid])
        b = self.merge_sort(L[mid:])
        return self.merge(a, b)