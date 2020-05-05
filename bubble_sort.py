#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bubble sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from base import Base
from typing import List

class BubbleSort(Base):
    def execute(self, L: List[int]) -> List[int]:
        for i in range(0, self.length):
            for j in range(i + 1, self.length):
                if L[i] > L[j]:
                    L[i], L[j] = L[j], L[i]
        return L

sort = BubbleSort()
sort.main()