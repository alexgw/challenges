#for day 2 - setup an array of the string numbers then can sub for the index of the loop and then run the same as befre
import re

#to solve https://adventofcode.com/2023/day/2
file = open('input.txt', 'r')
Lines = file.readlines()
 
count = 0
total = 0
# Strips the newline character
for line in Lines:
    count += 1

    numbers = re.sub("[^0-9]","",line) 
    #print("-----")
    #print(numbers)
    #print(line.strip())
    length = len(numbers)
    first = numbers[:1]
    last = numbers[(length-1):]
    #print(first)
    #print(last)
    val = first +last 
    value = int(val)
    total = total + value
    #print(total)
print(total)
