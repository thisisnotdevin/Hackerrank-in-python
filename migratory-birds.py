#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    birdCount = {}
    for bird in arr:
        if bird in birdCount:
            birdCount[bird] += 1
        else:
            birdCount[bird] = 1
    mostCommonBird = max(birdCount, key=birdCount.get)
    return min([bird for bird in birdCount if birdCount[bird] == birdCount[mostCommonBird]])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
