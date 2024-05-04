#for day 2 - setup an array of the string numbers then can sub for the index of the loop and then run the same as befre
"""
our calculation isn't quite right. It looks like some of the digits are 
actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine 
also count as valid "digits".
"""


'''
Currently not working think I've got too deep in regex - will come back 

'''

import re


string_numbers = ['one','two','three','four','five','six','seven','eight','nine']



#to solve https://adventofcode.com/2023/day/1 part two
file = open('input.txt', 'r')
Lines = file.readlines()
 
count = 0
total = 0
# Strips the newline character
for line in Lines:
    print(line)
    count += 1
    i = 0
    while i < len(string_numbers):
        #make a tuple of strings of numbers and other things in the line with regex
        line_num = re.split(".*?(one|two|three|four|five|six|seven|eight|nine)", line )

        for match in line_num:
            #Check we've got a match that's a number as a string
            if(re.search(".*?(one|two|three|four|five|six|seven|eight|nine)",match)):

                j = 0 
                while j < len(string_numbers):
                    #replace the string number with a numeric one using the index of string_numbers
                    if(match == string_numbers[j]):
                        line = line.replace(match, str(j+1))
                    j+=1
        i+=1
    #remove anything left that isn't a number    
    numbers = re.sub("[^0-9]","",line) 

    #get the length so we can splice the first and last numbers
    length = len(numbers)
    first = numbers[:1]
    last = numbers[(length-1):]
    
    #calculate the value and convert it to an into to be added to the total
    val = first +last 
    value = int(val)
    total = total + value
    print(val)
    print("running total: " + str(total))


#Print the total
print(total)
