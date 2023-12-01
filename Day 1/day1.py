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

with open('Day 1/day1.txt') as f:

    # regex expression to find the first substring that matches the values in the dict

    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six":6, "seven":7, "eight":8, "nine":9, 
             "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7": 7, "8":8, "9":9, "0":0}
    

    sum = 0
    for line in f:
        
        min_index = len(line) +10
        min_word = ""
        max_index = -10
        max_word = ""


        for word in words:

            if word in line:
                index = line.find(word)

                if index < min_index:
                    min_index = index
                    min_word = word

                index = line.rfind(word)

                if index > max_index:
                    max_index = index
                    max_word = word

        sum += words[min_word]*10 + words[max_word]


    print(sum)


    

