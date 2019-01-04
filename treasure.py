import pprint
from math import sqrt
from random import randint,shuffle
import pprint

def getDistant(obj1,obj2):
    xDistance = abs(obj1.getX()-obj2.getX())
    yDistance = abs(obj1.getY()-obj2.getY())

    distance = float(sqrt((xDistance*xDistance)+(yDistance*yDistance)))
    return distance


class Tools:
    def __init__(self,x=None,y=None):
        self.x=None
        self.y=None


        if x is not None:
            self.x=x
        else:
            self.x = randint(0,100)


        if y is not None:
            self.y=y
        else:
            self.y = randint(0,100)
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y


class gameAdmin():
    GamePoints = []

    def getPoints(self):

        NumberOfPoints = int(input('How many Points? \n'))
        choice = int(input('if you want to insert points enter 1 otherwise enter 0 \n'))
        if choice == 1:
            for i in range(NumberOfPoints):
                xaxis = int(input ('X [%s]'%i))
                yaxis = int(input('Y[%s]'%i))
                city = Tools(xaxis,yaxis)
                self.GamePoints.append(city)
     
        if choice == 0:
            for i in range(NumberOfPoints):
                city = Tools()
                print('x[%s] %s'%(i,city.getX()))
                print('y[%s] %s'%(i,city.getY()))
                self.GamePoints.append(city)
                
    def numberOfTools(self):
        return len(self.GamePoints)



class game:
    def __init__(self, gameAdmin):
        self.gameAdmin = gameAdmin

    def getPlayers(self):
        self.players = []
        self.numberOfplayers = int(input('How many players?'))
        for i in range(self.numberOfplayers):
            self.players.append(input('Enter Player[%s]:'%i))
                    
    def createMap(self):
        self.points = []
        self.points = gameAdmin.GamePoints
    
    def repre(self):
        for i in range(len(self.points)):
            print('[' + str(self.points[i].x) +','+ str(self.points[i].y) + ']' + '',end='')  
        print()     

    def chunks(self,l, n):
        for i in range(0, len(l), n):
            yield l[i:i+n]
    

    def playerPoint(self,):
        
        if int(len(self.points)/self.numberOfplayers)==len(self.points)/self.numberOfplayers:
            self.divider = int(len(self.points)/self.numberOfplayers)
        else:
            self.divider = int(len(self.points)/self.numberOfplayers)+1

        PlayerPoints = list(self.chunks(self.points,self.divider))
    
        for i in range(self.numberOfplayers):
            print(self.players[i] + '"s Goal',end='=')
            for j in range(len(PlayerPoints[i])):
                print('[' + str(PlayerPoints[i][j].x) +','+ str(PlayerPoints[i][j].y) + ']' + '',end='')  
            print('\n')

    def population(self,):
        FirstOne = self.points
        FirstGeneration = []
        NumberOfFirstGeneration = int(input('How many offsprings?'))
        for i in range(NumberOfFirstGeneration):
            shuffle(FirstOne)
            FirstGeneration.append(list(FirstOne))

        for i in range(NumberOfFirstGeneration):
            print()
            for j in range(len(FirstOne)):
                print('[' + str(FirstGeneration[i][j].x) +','+ str(FirstGeneration[i][j].y) + ']' + '',end='')  
        print()     
        
            



        
ali = gameAdmin() 
ali.getPoints()
treasure = game(ali)
treasure.getPlayers()
treasure.createMap()
treasure.repre()
treasure.playerPoint()
treasure.population()
# print('\n')
# a = ali.numberOfTools()
# print(a)
# city = Tools(10,20)
# city1 = Tools(20,30)

# a = float(getDistant(city,city1))
# print(a)
