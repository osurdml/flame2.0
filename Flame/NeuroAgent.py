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
        self.location = [50,50]
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
        input = [float(self.numbAgents[0])/10,float(self.numbAgents[1])/10,float(self.numbAgents[2])/10,float(self.numbAgents[3])/10,
                 float(self.distAgents[0])/3000,float(self.distAgents[1])/3000,float(self.distAgents[2])/3000,float(self.distAgents[3])/3000,
                 float(self.numbHotSpots[0])/50,float(self.numbHotSpots[1])/50,float(self.numbHotSpots[2])/50,float(self.numbHotSpots[3])/50,
                 float(self.distHotSpots[0])/3000,float(self.distHotSpots[1])/3000,float(self.distHotSpots[2])/3000,float(self.distHotSpots[3])/3000,
                 self.time,self.distToFireCenter/500]
        nNOutput = self.nNet.activate(input)
        m = max(nNOutput)
        self.actionTaken = [i for i, j in enumerate(nNOutput) if j == m]

    def takeAction(self):
        if(self.actionTaken[0] == 0):
            self.location[1] += 1
        elif(self.actionTaken[0] == 1):
            self.location[0] += 1
        elif(self.actionTaken[0] == 2):
            self.location[1] -= 1
        elif(self.actionTaken[0] == 3):
            self.location[0] -= 1

    def setTime(self, time):
        self.time = time
