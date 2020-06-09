#!/bin/python3
import os
import sys


def gradingStudents(grades):
    outputList = []
    for a0 in range(len(grades)):
        x = int(grades[a0])
        if x >= 38:
            if x % 5 > 2:
                while x % 5 != 0: x += 1
        outputList.append(x)
    return outputList


if __name__ == '__main__':
    helpCall = [44,84,94,21,0,18,100,18,62,30,61,53,0,43,2,29,53,61,40,14,4,29,98,37,23,46,9,79,62,20,38,51,99,59,47,4,86,61,68,17,45,6,1,95,95]
    result = gradingStudents(helpCall)
    print(str(result) + '\n')
