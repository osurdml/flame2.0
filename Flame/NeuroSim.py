#Frontier simulator 
from FrontierController import FrontierController
from NeuroFrontierConsumer import NeuroFrontierConsumer
from FarsiteProducer import FarsiteProducer
from TestScorer import TestScorer
#from Visualizer import Visualizer
import time
import numpy as np
import neurolab as nl


class NeuroSim():
    def __init__(self,NNet):
        self.frontierConsumer = NeuroFrontierConsumer(NNet)
        self.frontierConsumer2 = NeuroFrontierConsumer(NNet)
        self.frontierProducer = FarsiteProducer()
        self.scorer = TestScorer()
        self.frontierController = FrontierController(self.scorer,self.frontierProducer,[self.frontierConsumer, self.frontierConsumer2])

    def calcScore(self,NNet):
        i = 0
        totalScore = 0
        while(i < 10): #frontierController.hasData()):
            self.frontierController.tick()
            totalScore +=self.frontierConsumer.GetScore()
            #visualizer.vis(frontierController.frontierData)
            i = i +1
            #time.sleep(.1)
