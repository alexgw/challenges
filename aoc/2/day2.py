import re

file = open('input.txt', 'r')
Lines = file.readlines()

possible_games = []

for game in Lines:
    
    #get the number id of each game
    id = game.split(':')
    id = id[0];
    id = re.sub("[^0-9]","",id) 
    id = int(id)
    # get each round and split it out
    rounds= []

    rounds = game.split(':')
    rounds = rounds[1]
    rounds = rounds.split(';')
    #print(rounds)
    
    green = 0
    blue = 0
    red = 0

    for round in rounds:
        colours = round.split(",") 
        for colour in colours:
            num = re.sub("[^0-9]","",colour)
            if "blue" in colour:
                if int(num) > blue:
                    blue = int(num)
            if "red" in colour:
                if int(num) > red:
                    red = int(num)
            if "green" in colour:
                if int(num) > green:
                    green = int(num)

    
    #print("game: " + id + "had at most: " + str(green) + " green, " + str(red) + " red, and" + str(blue) + " blue.")

    if red <= 12 and green <= 13 and blue <=14:
        possible_games.append(id)


result = sum(possible_games)

print(result)
