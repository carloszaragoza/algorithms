#!/bin/python3

import os
import sys


def countApplesAndOranges(arr):
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
    s = 7
    t = 11
    a = 5
    b = 15
    m = 3
    n = 2
    apples = [-2, 2, 1]
    oranges = [5, -6]
    result = countApplesAndOranges(integerList)

    #print(str(result) + '\n')
