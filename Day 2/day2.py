import numpy
import math
import re

with open('Day 2/day2.txt') as f:
    sum = 0
    sum_powers = 0

    for game in f:
        id = game.split(" ")[1]
        ok = True

        max_blue, max_green, max_red = 0, 0, 0
        
        for set in game.strip().split(";"):
            red, green, blue = 0, 0, 0
            lim_red, lim_green, lim_blue = 12, 13, 14

            set = re.split(', | ', set)


            for i, word in enumerate(set):
                if word == "red":
                    temp = int(set[i-1])

                    if temp > max_red:
                        max_red = temp

                    red += temp

                elif word == "green":
                    temp = int(set[i-1])

                    if temp > max_green:
                        max_green = temp

                    green += temp

                elif word == "blue":
                    temp = int(set[i-1])
                    
                    if temp > max_blue:
                        max_blue = temp
                    
                    blue += temp

            if red > lim_red or green > lim_green or blue > lim_blue:
                ok = False

        power = max_red * max_green * max_blue
        sum_powers += power

        if ok:
            sum += int(id.strip(":"))
            print("Game ID possible: " + id, " Sum: ", sum, " Power: ", power)

            

print(sum)
print(sum_powers)
