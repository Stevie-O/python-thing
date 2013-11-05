from random import randint
i = randint(0,52)
f = open('C:/programs/Python/randomGameGenerator/gameList.txt', 'r')
game = f.readlines()
print game[i]

f = open('C:/programs/Python/randomGameGenerator/lastFinishedGame.txt', 'w')
f.write(game[i])