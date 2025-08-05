#!/bin/python3

import math
import os
import random
import re
import sys

#
# 256th day of an year is either Sep 13 or 12th Sep for a leap year

zero = 0

def dayOfProgrammer(year):
    if year == 1918:
        # Special transition year: Feb 14 is the 32nd day, so 256th day falls on Sep 26
        return f"26.09.{year}"
    elif year < 1918:
        # Julian calendar
        is_leap = year % 4 == 0
    else:
        # Gregorian calendar
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    day = 12 if is_leap else 13
    return f"{day:02d}.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result)

    fptr.close()
