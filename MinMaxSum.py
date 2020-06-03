#!/bin/python3

import os
import sys


def minMaxSum(arr):
    # Solution
    if len(arr) >= 1 and len(arr) <= 1e9:
        new = []
        for x in range(len(arr)):
            maximum = arr.copy()
            maximum.pop(x)
            new.append(sum(maximum))
        print(str(max(new)) + ' '+str(min(new)))


if __name__ == '__main__':

    integerList = [1, 2, 3, 4, 5]
    result = minMaxSum(integerList)

    #print(str(result) + '\n')
