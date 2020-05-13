#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""quick sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from .base import *
from typing import List
import copy

class QuickSort(Base):
    length = 10
    process = []

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        length = len(L)
        if length <= 1:
            return L

        self.quicksort(L, 0, length - 1)
        return L
    
    def partition(self, L: List[int], left: int, right: int) -> int:
        key = left
        while left < right:
            while left < right and L[right] >= L[key]:
                right -= 1
            while left < right and L[left] <= L[key]:
                left += 1
            L[left], L[right] = L[right], L[left]
            self.process.append(copy.deepcopy(L))
        L[left], L[key] = L[key], L[left]
        self.process.append(copy.deepcopy(L))
        return left

    def quicksort(self, L: List[int], left: int, right: int):
        if left >= right:
            return

        mid = self.partition(L, left, right)
        self.quicksort(L, left, mid - 1)
        self.quicksort(L, mid + 1, right)