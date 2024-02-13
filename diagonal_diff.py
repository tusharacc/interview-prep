#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    start = (0,0)
    r_inc, l_inc = 0, len(arr) - 1
    r_sum, l_sum = 0, 0
    for _ in range(len(arr)):
        r_index = (start[0] + r_inc, start[1] + r_inc)
        l_index = (start[0] + l_inc, (start[1] + l_inc)%len(arr))
        r_sum += arr[r_index[0]][r_index[1]]
        l_sum += arr[l_index[0]][l_index[1]]

    print (abs(r_sum - l_sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
