#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""main"""
__author__ = "funsoul"
__email__ = "cyanming2016@gmail.com"

import sys
from sorts.base import Base as BaseUtils
from sorts.bubble_sort import BubbleSort
from sorts.insertion_sort import InsertionSort
from sorts.cocktail_sort import CocktailSort
from sorts.bucket_sort import BucketSort
from sorts.counting_sort import CountingSort
from sorts.quick_sort import QuickSort
from sorts.merge_sort import MergeSort

if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 and int(sys.argv[1]) > 0 else 10

    baseUtils = BaseUtils(length)
    L = baseUtils.generator()
    baseUtils.print_list('List: ', L)

    # sort = BubbleSort(length)
    # sort.print_list('BubbleSort: ', sort.execute(L))
    # sort.save_animate()

    # sort = InsertionSort(length)
    # sort.print_list('InsertionSort: ', sort.execute(L))
    # sort.save_animate()

    # sort = CocktailSort(length)
    # sort.print_list('CocktailSort: ', sort.execute(L))
    # sort.save_animate()

    # sort = BucketSort(length)
    # sort.print_list('BucketSort: ', sort.execute(L))

    # sort = CountingSort(length)
    # sort.print_list('CountingSort: ', sort.execute(L))

    # sort = QuickSort(length)
    # sort.print_list('QueueSort: ', sort.execute(L))
    # sort.save_animate()

    sort = MergeSort(length)
    sort.print_list('MergeSort: ', sort.execute(L))
    # sort.save_animate()