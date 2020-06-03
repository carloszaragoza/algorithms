#!/bin/python3

import os
import sys


def staircase(n):
    # Solution
    for x in range(n):
        repit = (n-1)-x
        repitNumeral = x+1
        spaces = ' '*repit
        numeral = '#'*repitNumeral
        print(spaces+numeral)


if __name__ == '__main__':

    result = staircase(6)
