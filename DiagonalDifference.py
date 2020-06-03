#!/bin/python3

import os
import sys

def diagonalDIfference(arr):
    # Solution
    if len(arr) >= -100 and len(arr) <= 100:
        diagonal_one = 0
        diagonal_two = 0

        for x in range(len(arr)):
            nextList = [item[x] for item in arr]
            diagonal_one += nextList[x]
            diagonal_two += nextList[-(x+1)]
    return abs(diagonal_one - diagonal_two)

if __name__ == '__main__':

    diagonalMatrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDIfference(diagonalMatrix)

    print(str(result) + '\n')
