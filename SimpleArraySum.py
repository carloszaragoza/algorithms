#!/bin/python3

import os
import sys

def simpleArraySum(ar):
    #Solution
    suma = 0
    for x in range (len(ar)):
        suma += ar[x]

    return suma


if __name__ == '__main__':
 
    ar = [1,2,3]

    result = simpleArraySum(ar)

    print(str(result) + '\n')
