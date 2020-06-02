#!/bin/python3

import os
import sys


def plusMinus(arr):
    # Solution
    positive = 0
    negative = 0
    zero = 0
    size = len(arr)
    if size > 0 and size <= 100:
        for x in range(size):
            if arr[x] > 0:
                positive += 1
            if arr[x] < 0:
                negative += 1
            if arr[x] == 0:
                zero += 1
    positive = float("{:.6f}".format(positive/size))
    negative = float("{:.6f}".format(negative/size))
    zero = float("{:.6f}".format(zero/size))

    print(str(positive) + '\n' + str(negative) + '\n' + str(zero))


if __name__ == '__main__':

    matrix = [-4, 3, -9, 0, 4, 1]

    result = plusMinus(matrix)
