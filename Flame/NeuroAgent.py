from abc import ABCMeta, abstractmethod
from Agent import Agent
from random import randint
import math


class NeuroAgent(Agent):

    def __init__(self,NNet):
        self.nNet = NNet
        self.numbAgents = [0,0,0,0]
        self.distAgents =[0,0,0,0]
        self.numbHotSpots = [0,0,0,0]
        self.distHotSpots = [0,0,0,0]
        self.timeElapsed = 0
        self.distToFireCenter = 0
        self.score = 0
        self.actionTaken = 0
        self.location = [50,50]

    def consumeFilterData(self, filterData):
        self.timeElapsed = randint(1,10)
        self.numbAgents = [randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
        self.distAgents =[randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
        self.numbHotSpots = [randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
        self.distHotSpots = [randint(1,10),randint(1,10),randint(1,10),randint(1,10)]
        self.timeElapsed = randint(1,10)
        self.distToFireCenter = randint(1,10)
        self.calcActionTaken()
        self.takeAction()

    def updateScore(self,score):
        self.score = score

    def getScore(self):
        return self.score

    def getLocation(self):
        return self.location


    def calcActionTaken(self):
        input = [self.numbAgents[0],self.numbAgents[1],self.numbAgents[2],self.numbAgents[3],
                 self.distAgents[0],self.distAgents[1],self.distAgents[2],self.distAgents[3],
                 self.numbHotSpots[0],self.numbHotSpots[1],self.numbHotSpots[2],self.numbHotSpots[3],
                 self.distHotSpots[0],self.distHotSpots[1],self.distHotSpots[2],self.distHotSpots[3],
                 self.timeElapsed,self.distToFireCenter]
        self.actionTaken = math.floor(self.nNet.activate(input)*4)  #Assuming it returns a number 0-1

    def takeAction(self):
        if(self.actionTaken ==1):
            self.location[1] += 1
        elif(self.actionTaken ==2):
            self.location[0] += 1
        elif(self.actionTaken ==3):
            self.location[1] -= 1
        elif(self.actionTaken ==4):
            self.location[0] -= 1

