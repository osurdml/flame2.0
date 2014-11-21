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
        self.neuroAgent1 = NeuroAgent(NNet)
        self.neuroAgent2 = NeuroAgent(NNet)
        self.frontierProducer = FarsiteProducer()
        self.scorer = NeuroScorer()
        self.hotSpotFilter = HotspotFilter()
        self.fovFilter = FovFilter()
        self.visualization = visualization
        self.frontierController = FrontierController(self.scorer,self.frontierProducer,[self.neuroAgent1, self.neuroAgent2], [self.hotSpotFilter, self.fovFilter])

    def calcScore(self):
        i = 0
        visualizer = Visualizer()
        totalScore = 0
        iterations = 10
        if (self.visualization == 1):
            iterations = 1000


        while(i < iterations): #frontierController.hasData()):
            self.frontierController.tick()
            totalScore += self.neuroAgent1.getScore()
            if (self.visualization == 1):
                visualizer.vis(self.frontierController.frontierData, self.frontierController.agentLocations)
            i = i +1
