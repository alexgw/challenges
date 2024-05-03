#for day 2 - setup an array of the string numbers then can sub for the index of the loop and then run the same as befre
"""
our calculation isn't quite right. It looks like some of the digits are 
actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine 
also count as valid "digits".
"""


import re


string_numbers = ['one','two','three','four','five','six','seven','eight','nine']



#to solve https://adventofcode.com/2023/day/1 part two
file = open('demo.txt', 'r')
Lines = file.readlines()
 
count = 0
total = 0
# Strips the newline character
for line in Lines:
    count += 1
    i = 0
    print("-----")
    print(line.strip())
    while i < len(string_numbers):
        # (one|two|three|four|five|six|seven|eight|nine) matches in order but how to swap..
        #bug with eightwo because two is matched before eight the t is chopped off eight should match eight as it comes first...
        #print("checking for " + string_numbers[i])
        line = re.sub("("+string_numbers[i]+ ")",str(i+1),line)
        #print("swapped: " + string_numbers[i] + " for " + str(i+1)) 
        i+=1
    print(line.strip())
    numbers = re.sub("[^0-9]","",line) 
    print(numbers)
    #print(line.strip())
    length = len(numbers)
    first = numbers[:1]
    last = numbers[(length-1):]
    val = first +last 
    value = int(val)
    total = total + value
    print(val)
    print("running total: " + str(total))
print(total)
