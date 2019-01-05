import pprint
from math import sqrt
from random import randint,shuffle,choice
import pprint
import os
import sys
import numpy

#Clear function to clear screen in any OS
def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


#Spot of each tool will add in this class

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


#Function for administrator of game, to add points using Tools class

class gameAdmin():
    GamePoints = []

    def getPoints(self):

        NumberOfPoints = int(input("Number Of Points : \n"))
        print('Options:')
        print('Press 0 : Random enterance \nPress 1 : Entering point from keyboard')
        choice = int(input(''))
        if choice == 1:
            for i in range(NumberOfPoints):
                xaxis = int(input('X[%s]'%i))
                yaxis = int(input('Y[%s]'%i))
                city = Tools(xaxis,yaxis)
                self.GamePoints.append(city)
     
        if choice == 0:
            for i in range(NumberOfPoints):
                city = Tools()
                print('x[%s] %s'%(i,city.getX()),',','y[%s] %s'%(i,city.getY()),end=' ')
                self.GamePoints.append(city)
        
    def numberOfTools(self):
        return len(self.GamePoints)


#All of the game details is in this class
class game:
    def __init__(self, gameAdmin):
        self.gameAdmin = gameAdmin


#get distance of two points for each player
    def getDistant(self,obj1,obj2):
        xDistance = abs(obj1.x-obj2.x)
        yDistance = abs(obj1.y-obj2.y)

        self.distance = float(sqrt((xDistance*xDistance)+(yDistance*yDistance)))
        return self.distance

#Get information of players
    def getPlayers(self):
        self.players = []
        self.numberOfplayers = int(input('Number Of Player:'))
        for i in range(self.numberOfplayers):
            self.players.append(input('Player[%s]:'%i))

#create map of the game using the points that admin has entered              
    def createMap(self):
        self.points = []
        self.points = gameAdmin.GamePoints
    
#Representation of each chromosome
    def repre(self):
        for i in range(len(self.points)):
            print('[' + str(self.points[i].x) +','+ str(self.points[i].y) + ']' + '',end='')  
        print()     

#Divide each chromosome
    def chunks(self,l, n):
        for i in range(0, len(l), n):
            yield l[i:i+n]
    

#Assign and show each player spot of each tool to go and possess them
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

#Here is the main part of the game
#we create first chromosome using points
#by using shuffle we create first generation of possible answers
#then we add each combination to FirstGeneration
    def population(self,):
        FirstOne = self.points
        self.FirstGeneration = []
        self.NumberOfFirstGeneration = int(input('Number Of First Generation:'))
        for i in range(self.NumberOfFirstGeneration):
            shuffle(FirstOne)
            self.FirstGeneration.append(list(FirstOne))

        for i in range(self.NumberOfFirstGeneration):
            print()
            for j in range(len(FirstOne)):
                print('[' + str(self.FirstGeneration[i][j].x) +','+ str(self.FirstGeneration[i][j].y) + ']' + '',end='')  
        print()     



#we chunk each possibe answer which is in FirstGeneration to parts for each player
#then we use getDistant function to process the Fitness of each answer
#we have three different level for game and by using different fitness function ,
#we Distinguish between levels, 0 -> easy , 1 -> normal , 2 -> hard

#We add each Fitness value to Fitness and by using index we map it to each answer
    def fitnessFunction(self,level):
        self.Fitness=[]
        for i in range(len(self.FirstGeneration)): 

            GenerationPlayerPoints = list(self.chunks(self.FirstGeneration[i],self.divider))
            eachFitness=0   

            for j in range(len(self.players)):
                PlayersGoals= GenerationPlayerPoints[j]

                for k in range(len(PlayersGoals)-1):
                    eachFitness = eachFitness + self.getDistant(PlayersGoals[k],PlayersGoals[k+1])
            if level==0:
                self.Fitness.append(1/eachFitness)
            if level==1:
                            self.Fitness.append(1/eachFitness*eachFitness)            
            if level==2:
                            self.Fitness.append(1/eachFitness*eachFitness*eachFitness)
        for i in range(len(self.Fitness)):
            print(self.Fitness[i],sep=',')


    def selection(self,percentage):
        self.SelectedFirstGeneration = []
        print()        
        for i in range(int((percentage/100)*len(self.FirstGeneration))+1):
            self.SelectedFirstGeneration.append(self.FirstGeneration[self.Fitness.index(max(self.Fitness))])
            self.Fitness[self.Fitness.index(max(self.Fitness))] = 0
            



        print('Selection')
        for i in range(len(self.SelectedFirstGeneration)):
            for j in range(len(self.points)):
                print(self.SelectedFirstGeneration[i][j].x,',',self.SelectedFirstGeneration[i][j].y,end='')
            print()







    def crossOver(self,number):
        for i in range(number):
            obj1 = choice(self.FirstGeneration)

            print('Object1:',end='')
            for j in range(len(obj1)):
                print(str(obj1[j].x)+','+str(obj1[j].y),end=' ')
            print()




            obj2 = choice(self.FirstGeneration)

            print('Object2:',end='')
            for j in range(len(obj1)):
                print(str(obj2[j].x)+','+str(obj2[j].y),end=' ')
            print()


            p1=[]
            p2=[]

            for j in range(int(0.2*len(self.points))):
                m=choice(obj1)
                p1.append(m)

            for k in range(0,len(p1)):
                p2.append(obj2.index(p1[k]))
                print(obj2.index(p1[k]))
            p2.sort()

            p1InOrder= []            
            for k in range(len(p1)):
                p1InOrder.append(obj1.index(p1[k]))
                print('p1InOrder',p1InOrder)
            p1InOrder.sort()
            print('sorted p1:',*p1InOrder)

            for t in range(len(p1)):
                print(str(p1[t].x)+','+str(p1[t].y),end=' ')
            print()

            
            for d in range(len(p2)):
                print('len(p1)',len(p1))
                print('____________________________________________')

                print('obj1[p1InOrder]',obj1[p1InOrder[d]].x,':',obj1[p1InOrder[d]].y)
                print('obj2[p2[d]]',obj2[p2[d]].x,':',obj2[p2[d]].y)
                obj1[p1InOrder[d]] = obj2[p2[d]]

                # print("obj1[obj1.index(p1[d])]",obj1[obj1.index(p1[d])].x,obj1[obj1.index(p1[d])].y)
                
            self.SelectedFirstGeneration.append(obj1)

            for i in range(len(self.SelectedFirstGeneration)):
                for j in range(len(self.points)):
                    print(self.SelectedFirstGeneration[i][j].x,',',self.SelectedFirstGeneration[i][j].y,end='  ')
                print()

            print('CrossOver',end='')
            for j in range(len(obj1)):
                print(str(obj1[j].x)+','+str(obj1[j].y),end=' ')
            print() 
            print(')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        print()
    
    def mutation(self,percentage):
        
        for i in range(int((len(self.SelectedFirstGeneration)*percentage/100)+1)):
            MutationOne = list(choice(self.SelectedFirstGeneration))

            MutationOneIndex = self.SelectedFirstGeneration.index(MutationOne)

            a = MutationOne.index(choice(MutationOne))
            b = MutationOne.index(choice(MutationOne))
            
            self.SelectedFirstGeneration[MutationOneIndex][a],self.SelectedFirstGeneration[MutationOneIndex][b] =self.SelectedFirstGeneration[MutationOneIndex][b],self.SelectedFirstGeneration[MutationOneIndex][a]
            

   
        for i in range(len(self.SelectedFirstGeneration)):
            for j in range(len(self.points)):
                print(self.SelectedFirstGeneration[i][j].x,',',self.SelectedFirstGeneration[i][j].y,end='  ')
            print()


    def generation(self,):
        numberOfGeneration = input('How many generations do you want to create?')
        self.FirstGeneration = self.SelectedFirstGeneration
        for i in range(int(numberOfGeneration)):
            print('Generation___________________%s'%i)
            self.fitnessFunction(0)
            self.selection(30)
            self.crossOver(2)
            self.mutation(10)
        self.FirstGeneration = self.SelectedFirstGeneration
        return self.SelectedFirstGeneration



ali = gameAdmin() 
ali.getPoints()
treasure = game(ali)
treasure.getPlayers()
treasure.createMap()
clear()
treasure.repre()
treasure.playerPoint()
treasure.population()
treasure.fitnessFunction(0)

treasure.selection(30)
treasure.crossOver(2)
treasure.mutation(10)
treasure.generation()