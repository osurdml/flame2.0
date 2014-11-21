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
        self.distToFireCenter = 0
        self.score = 0
        self.actionTaken = 0
        self.location = [randint(1,200),randint(1,200)]
        self.time = 0

    def consumeFilterData(self, filterData):
        self.numbAgents = [filterData[0],filterData[2],filterData[4],filterData[6]]
        self.distAgents =[filterData[1],filterData[3],filterData[5],filterData[7]]
        self.numbHotSpots = [filterData[8],filterData[10],filterData[12],filterData[14]]
        self.distHotSpots = [filterData[9],filterData[11],filterData[13],filterData[15]]
        self.distToFireCenter = filterData[16]
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
                 self.time,self.distToFireCenter]
        self.actionTaken = math.floor(self.nNet.activate(input)%4+1)  #Assuming it returns a number 0-1

    def takeAction(self):
        if(self.actionTaken ==1):
            self.location[1] += 1
        elif(self.actionTaken ==2):
            self.location[0] += 1
        elif(self.actionTaken ==3):
            self.location[1] -= 1
        elif(self.actionTaken ==4):
            self.location[0] -= 1

    def setTime(self, time):
        self.time = time
