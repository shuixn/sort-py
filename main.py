#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""main"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

import sys
from sorts.base import Base as BaseUtils
from sorts.bubble_sort import BubbleSort
from sorts.insertion_sort import InsertionSort

if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 and int(sys.argv[1]) > 0 else 10

    baseUtils = BaseUtils(length)
    L = baseUtils.generator()
    baseUtils.print_list('List: ', L)

    sort = BubbleSort(length)
    sort.print_list('BubbleSort: ', sort.execute(L))

    sort = InsertionSort(length)
    sort.print_list('InsertionSort: ', sort.execute(L))