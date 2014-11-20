#Frontier simulator
from FovFilter import FovFilter
from FrontierController import FrontierController
from HotspotFilter import HotspotFilter
from NeuroAgent import NeuroAgent
from FarsiteProducer import FarsiteProducer
from NeuroScorer import NeuroScorer
from TestScorer import TestScorer
from Visualizer import Visualizer
import time
import numpy as np
#import neurolab as nl
from pybrain.structure import FeedForwardNetwork


class NeuroSim():
    def __init__(self,NNet,visualization):
        self.frontierConsumer = NeuroAgent(NNet)
        self.frontierConsumer2 = NeuroAgent(NNet)
        self.frontierProducer = FarsiteProducer()
        self.scorer = NeuroScorer()
        self.hotSpotFilter = HotspotFilter()
        self.fovFilter = FovFilter()
        self.visualization = visualization
        self.frontierController = FrontierController(self.scorer,self.frontierProducer,[self.frontierConsumer, self.frontierConsumer2], [self.hotSpotFilter, self.fovFilter])

    def calcScore(self):
        i = 0
        visualizer = Visualizer()
        totalScore = 0
        while(i < 10): #frontierController.hasData()):
            self.frontierController.tick()
            totalScore = self.frontierConsumer.getScore()
            #visualizer.vis(frontierController.frontierData)
            if (self.visualization == 1):
                visualizer.vis(self.frontierController.frontierData, self.frontierController.agentLocations)
            i = i +1
            #time.sleep(.1)
