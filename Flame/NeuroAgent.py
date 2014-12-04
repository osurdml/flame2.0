from abc import ABCMeta, abstractmethod
from Agent import Agent
from random import randint
import math


class NeuroAgent(Agent):

    def __init__(self,NNet):
        self.nNet = NNet
        self.numbAgents = [0,0,0,0]
        #self.distAgents =[0,0,0,0]
        self.distNearHS = 0
        self.numbHotSpots = [0,0,0,0]
        #self.distHotSpots = [0,0,0,0]
        self.distToFireCenter = 0
        self.score = 0
        self.actionTaken = 0

        self.location = [20,20]
        #rand = randint(1,4)
        #if(rand == 1):
            #self.location = [randint(1,10),randint(1,10)]
        #elif(rand == 2):
            #self.location = [randint(1,10),randint(90,100)]
        #elif(rand == 3):
            #self.location = [randint(90,100),randint(90,100)]
        #else:
            #self.location = [randint(90,100),randint(1,10)]
        self.time = 0

    def consumeFilterData(self, filterData):
        self.numbAgents = [filterData[4],filterData[5],filterData[6],filterData[7]]
        self.numbHotSpots = [filterData[0],filterData[1],filterData[2],filterData[3]]
        self.distNearHS = filterData[8]
        #self.numbAgents = [filterData[0],filterData[2],filterData[4],filterData[6]]
        #self.distAgents =[filterData[1],filterData[3],filterData[5],filterData[7]]
        #self.numbHotSpots = [filterData[8],filterData[10],filterData[12],filterData[14]]
        #self.distHotSpots = [filterData[9],filterData[11],filterData[13],filterData[15]]
        #self.locationOfFireCenter = filterData[16]
        self.calcActionTaken()
        self.takeAction()

    def updateScore(self,score):
        self.score = score

    def getScore(self):
        return self.score

    def getLocation(self):
        return self.location


    def calcActionTaken(self):
        #input = [float(self.numbAgents[0])/10,float(self.numbAgents[1])/10,float(self.numbAgents[2])/10,float(self.numbAgents[3])/10,
        #         float(self.distAgents[0])/200,float(self.distAgents[1])/200,float(self.distAgents[2])/200,float(self.distAgents[3])/200,
        #         float(self.numbHotSpots[0])/50,float(self.numbHotSpots[1])/50,float(self.numbHotSpots[2])/50,float(self.numbHotSpots[3])/50,
        #         float(self.distHotSpots[0])/200,float(self.distHotSpots[1])/200,float(self.distHotSpots[2])/200,float(self.distHotSpots[3])/200,
        #         self.time,self.locationOfFireCenter/4]

        input = [float(self.numbAgents[0])/2,float(self.numbAgents[1])/2,float(self.numbAgents[2])/2,float(self.numbAgents[3])/2,
                 float(self.numbHotSpots[0])/2,float(self.numbHotSpots[1])/2,float(self.numbHotSpots[2])/2,float(self.numbHotSpots[3])/2,
                 self.distNearHS/300,self.time]

        fourInputCase = [float(self.numbHotSpots[0])/2,float(self.numbHotSpots[1])/2,float(self.numbHotSpots[2])/2,float(self.numbHotSpots[3])/2]
        nNOutput = self.nNet.activate(input)
        m = max(nNOutput)
        self.actionTaken = [i for i, j in enumerate(nNOutput) if j == m]

    def takeAction(self):
        if(self.actionTaken[0] == 0):
            self.location[1] += 1
            self.location[0] += 1
        elif(self.actionTaken[0] == 1):
            self.location[1] -= 1
            self.location[0] += 1
        elif(self.actionTaken[0] == 2):
            self.location[1] += 1
            self.location[0] -= 1
        elif(self.actionTaken[0] == 3):
            self.location[1] -= 1
            self.location[0] -= 1

    def setTime(self, time):
        self.time = time
