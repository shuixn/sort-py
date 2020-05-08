#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cocktail sort"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

from .base import *
from typing import List
import copy

class CocktailSort(Base):
    length = 10
    process = []

    def __init__(self, length: int = 10):
        self.length = length

    @CaculateTime
    def execute(self, L: List[int]) -> List[int]:
        self.process.append(copy.deepcopy(L))
        flag = True
        for i in range(len(L) // 2):
            if flag:
                flag = False
                for j in range(i,len(L) - i - 1):
                    if L[j] > L[j+1]:
                        L[j], L[j+1] = L[j+1], L[j]
                        flag = True
                        self.process.append(copy.deepcopy(L))

                for j in range(len(L) - 1 - i, i, -1):
                    if L[j] < L[j-1]:
                        L[j], L[j-1] = L[j-1], L[j]
                        flag = True
                        self.process.append(copy.deepcopy(L))
            else:
                break
        return L