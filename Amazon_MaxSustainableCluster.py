#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMaximumSustainableClusterSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processingPower
#  2. INTEGER_ARRAY bootingPower
#  3. LONG_INTEGER powerMax
#

def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
    """
    ids -> 1,2,3
    power -> power[i]
    can only cluser subsequent porcessors
    seems like a sliding window problem
    """
    
    window_start = 0
    max_cluster = 0
    
    for window_end in range(len(processingPower)):
        total_power = calculateTotalPower(window_start, window_end,processingPower, bootingPower)
        if total_power <= powerMax:
            max_cluster = max(max_cluster, window_end-window_start +1)
        else:
            window_start += 1
    
    return max_cluster

def calculateTotalPower(start, end, processingPower, bootingPower):
    max_bp = max(bootingPower[start: end+1]) #probably why this is timing out, slicing
    bp = sum(processingPower[start:end+1]) * (end-start +1)
    
    return max_bp + bp
    

