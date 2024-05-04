import re

file = open('input.txt', 'r')
Lines = file.readlines()

power_of_games = []

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
    
    green = []
    blue = []
    red = []

    for round in rounds:
        colours = round.split(",") 
        for colour in colours:
            num = re.sub("[^0-9]","",colour)
            if "blue" in colour:
                blue.append(int(num))
            if "red" in colour:
                red.append(int(num))
            if "green" in colour:
                green.append(int(num))

    
    #print("game: " + id + "had at most: " + str(green) + " green, " + str(red) + " red, and" + str(blue) + " blue.")

    power = max(blue) * max(green) * max(red) 
    print(max(red), max(green), max(blue), power)
    power_of_games.append(power)

result = sum(power_of_games)

print(result)
