#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    numSwaps = 0
    #n = a.len()
    # Write your code here
    for i in range(0, len(a)-1 ):
        for j in range (0, len(a)- 1):
        #Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                a[j] , a[j + 1] = a[j + 1] , a[j]
                numSwaps +=1
    print("Array is sorted in" + " "  +  str(numSwaps) +  " " + "swaps.")
    print("First Element:" + " " +  str(a[0]))
    print("Last Element:"  + " " +  str(a[n - 1]))
        
    
    


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
