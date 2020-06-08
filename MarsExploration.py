#!/bin/python3
import os
import sys


def marsExploration(s):
    # Solution
    call = 'SOS'
    x = 0
    iterator = len(s) / 3
    call = call*int(iterator)
    print(call)
    for i in range(len(s)):
        if call[i] != s[i]:
            x = x + 1
    return x

if __name__ == '__main__':
    helpCall = 'SOSSOT'
    result = marsExploration(helpCall)
    print(str(result) + '\n')
