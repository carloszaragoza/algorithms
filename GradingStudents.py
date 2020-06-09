#!/bin/python3
import os
import sys


def gradingStudents(grades):
    if len(grades) >= 1 and len(grades) <= 60:
        outputList = []
        for grade in range(len(grades)):
            if int(grades[grade])>=0 and int(grades[grade]) <=100:
                if int(grades[grade]) < 38:
                    outputList.append(grades[grade])
                else:
                    if int(grades[grade]) >= 10:
                        numberFinal = grades[grade] % 10
                        if numberFinal == 4 or numberFinal == 9:
                            numberFinal = int(grades[grade]) + 1
                            outputList.append(int(numberFinal))
                        elif numberFinal == 3 or numberFinal == 8:
                            numberFinal = int(grades[grade]) + 2
                            outputList.append(int(numberFinal))
                        else:
                            outputList.append(grades[grade])
                    else:
                        outputList.append(grades[grade])
    return outputList


if __name__ == '__main__':
    helpCall = [44,84,94,21,0,18,100,18,62,30,61,53,0,43,2,29,53,61,40,14,4,29,98,37,23,46,9,79,62,20,38,51,99,59,47,4,86,61,68,17,45,6,1,95,95]
    result = gradingStudents(helpCall)
    print(str(result) + '\n')
