#!/bin/python3

import os
import sys

def compareTheTriplets(a,b):
    #Solution
    alice = 0
    bob = 0
    ar = []
    for x in range(3):
        if(a[x] > b[x]):
            alice += 1
        if(a[x] < b[x]):
            bob +=1
    ar.append(alice)
    ar.append(bob)
    return ar


if __name__ == '__main__':

    alice = [1,2,3]
    bob = [3,2,1]

    result = compareTheTriplets(alice, bob)

    print(str(result) + '\n')
