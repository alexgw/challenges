
import re

#to solve https://adventofcode.com/2023/day/1 
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
