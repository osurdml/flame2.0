#Frontier simulator 
from FrontierController import FrontierController
from NeuroFrontierConsumer import NeuroFrontierConsumer
from FarsiteProducer import FarsiteProducer
from NeuroScorer import NeuroScorer
from TestScorer import TestScorer
#from Visualizer import Visualizer
import time
import numpy as np
#import neurolab as nl
from pybrain.structure import FeedForwardNetwork


class NeuroSim():
    def __init__(self,NNet):
        self.frontierConsumer = NeuroFrontierConsumer(NNet)
        self.frontierConsumer2 = NeuroFrontierConsumer(NNet)
        self.frontierProducer = FarsiteProducer()
        self.scorer = NeuroScorer()
        #self.hotSpotFilter = Filters()
        #self.agentFilter = Filters()
        self.frontierController = FrontierController(self.scorer,self.frontierProducer,[self.frontierConsumer, self.frontierConsumer2])

    def calcScore(self):
        i = 0
        totalScore = 0
        while(i < 10): #frontierController.hasData()):
            self.frontierController.tick()
            totalScore = self.frontierConsumer.getScore()
            #visualizer.vis(frontierController.frontierData)
            i = i +1
            #time.sleep(.1)
