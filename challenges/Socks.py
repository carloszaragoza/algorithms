#!/bin/python3
import os
import sys


def socks():
    return "s"


def socks(days, states):
    return "s and d"


def cells(days, states):
    # Solution
    d = days
    c = states
    left = 0
    rigth = 0
    result = []
    for day in range(d):
        for x in range(len(c)):
            if x == 0:
                result.append(0 if 0 == c[x + 1] else 1)
            elif x == len(c) - 1:
                result.append(0 if c[x] == 0 else 1)
            elif x > 0 and x < len(c) - 1:
                result.append(0 if c[x - 1] == c[x + 1] else 1)

    print(convert(result))


if __name__ == '__main__':
    days = 1
    cells = [1, 0, 0, 0, 0, 1, 0, 0]
    result = socks(days, cells)
    print(str(result) + '\n')
    # AMCAT 23280720363410
