import numpy
import math
import re

with open('Day 1/day1.txt') as f:
    sum = 0
    for line in f:
        l = line.strip()

        found_f = False
        found_l = False

        num1 = 0
        num2 = 0
        for char in l:
            #print("In forward: " + char, " Num1: " + str(num1))
            if char.isdigit():
                num1 = int(char)
                break

        for char in reversed(l):
            #print("In reverse: " + char, " Num2: " + str(num2))
            if char.isdigit():
                num2 = int(char)
                break

        sum += num1*10+num2

    print(sum)



    

