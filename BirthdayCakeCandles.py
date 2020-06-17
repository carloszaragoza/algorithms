#!/bin/python3
import os
import sys


def birthdayCakeCandles(ar):
    # Solution
    print(str(ar.count(max(ar))))


if __name__ == '__main__':
    height_of_candle = [3, 2, 1, 3]
    result = birthdayCakeCandles(height_of_candle)
    #print(str(result) + '\n')
 