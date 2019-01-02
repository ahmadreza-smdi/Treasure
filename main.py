
from random import randint,choice



#First we get number of points and players

numberOfPoints = int(input('How many points do you need? \n'))
numberOfPlayers = int(input('How many players ?'))

nameOfPlayer = []
for i in range(numberOfPlayers):
    nameOfPlayer.append(input('Write name [%s] :'%i))

# just create a rising list of numbers
X_axis = []
for i in range(numberOfPoints):
    X_axis.append(i)
    
#chunks function for partitioning the points for players    
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

#Representation
def Repre():
    
    RepreList = {}
    for i in range(numberOfPoints):
        randomPoints = randint(0,numberOfPoints-1)
        RepreList.update({i:randomPoints})
    
    if int(numberOfPoints/numberOfPlayers)==numberOfPoints/numberOfPlayers:
        divider = int(numberOfPoints/numberOfPlayers)
    else:
        divider = int(numberOfPoints/numberOfPlayers)+1

    PlayerPoints = list(chunks(X_axis,divider))

    player = []
   

    for i in range(len(PlayerPoints)):
        player.append(len(PlayerPoints[i]))
    
    for i in range(len(nameOfPlayer)):
        
        print(nameOfPlayer[i],':',PlayerPoints[i])

    for key,val in RepreList.items():
        print (key, "=>", val)
Repre()



