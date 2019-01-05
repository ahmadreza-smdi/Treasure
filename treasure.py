import pprint
from math import sqrt
from random import randint,shuffle,choice
import pprint
import os
import sys
import numpy

def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


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

    def getDistant(self,obj1,obj2):
        xDistance = abs(obj1.x-obj2.x)
        yDistance = abs(obj1.y-obj2.y)

        self.distance = float(sqrt((xDistance*xDistance)+(yDistance*yDistance)))
        return self.distance

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
        self.FirstGeneration = []
        self.NumberOfFirstGeneration = int(input('How many offsprings?'))
        for i in range(self.NumberOfFirstGeneration):
            shuffle(FirstOne)
            self.FirstGeneration.append(list(FirstOne))

        for i in range(self.NumberOfFirstGeneration):
            print()
            for j in range(len(FirstOne)):
                print('[' + str(self.FirstGeneration[i][j].x) +','+ str(self.FirstGeneration[i][j].y) + ']' + '',end='')  
        print()     
        
    def fitnessFunction(self,):
        self.Fitness=[]
        for i in range(self.NumberOfFirstGeneration): 

            GenerationPlayerPoints = list(self.chunks(self.FirstGeneration[i],self.divider))
            eachFitness=0   

            for j in range(len(self.players)):
                PlayersGoals= GenerationPlayerPoints[j]

                for k in range(len(PlayersGoals)-1):
                    eachFitness = eachFitness + self.getDistant(PlayersGoals[k],PlayersGoals[k+1])
            
            self.Fitness.append(1/eachFitness)
        
        for i in range(len(self.Fitness)):
            print(self.Fitness[i],sep=',')
        p = [] 
        # p = max(Fitness)
        # g = Fitness.index(p)
        # c = self.FirstGeneration[Fitness.index(Fittest[i])]
        # print()
        # for i in range(len(self.FirstGeneration[g])):
        #     print(c[i].x,c[i].y,end=',')

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
                # p3.append(obj1.index(m))
                # print('teeeeest')
                # print(p3[j])
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
            # zipP1 = list(zip(p1InOrder,p1))
            # zipP1.sort()
            # p1_sorted = [p1 for p1InOrder, p1 in zipP1]
            # p1 = p1_sorted
            # print('P2:',end='')
            # print(*p2)


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
    
        
        






        
ali = gameAdmin() 
ali.getPoints()
treasure = game(ali)
treasure.getPlayers()
treasure.createMap()
clear()
treasure.repre()
treasure.playerPoint()
treasure.population()
treasure.fitnessFunction()

treasure.selection(10)
treasure.crossOver(2)
# print('\n')
# a = ali.numberOfTools()
# print(a)
# city = Tools(10,20)
# city1 = Tools(20,30)

# a = float(getDistant(city,city1))
# print(a)
