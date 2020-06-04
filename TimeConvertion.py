#!/bin/python3
import os
import sys


def timeConvertion(s):
    # Solution
    time = s.split(':')
    final = time[2]
    if 'PM' in time[2]:
        firt_hour = '12' if time[0] == '12' else time[0]+12
        result = str(firt_hour) +':'+ time[1] + ':' + str(final[:-2])
    if 'AM' in time[2]:
        firt_hour='00' if time[0] == '12' else time[0]
        result = firt_hour + ':' + time[1] + ':' + str(final[:-2])

    return result

if __name__ == '__main__':
    today='12:45:54PM'
    result=timeConvertion(today)
    print(str(result) + '\n')
