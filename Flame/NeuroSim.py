#Frontier simulator
from FovFilter import FovFilter
from FrontierController import FrontierController
from HotspotFilter import HotspotFilter
from NeuroAgent import NeuroAgent
from FarsiteProducer import FarsiteProducer
from NeuroScorer import NeuroScorer
from SimpleFovFilter import SimpleFovFilter
from SimpleHotspotFilter import SimpleHotspotFilter
from SimpleProducer import SimpleProducer
from SimpleScorer import SimpleScorer
from TestScorer import TestScorer
from Visualizer import Visualizer
import time
import numpy as np
from pybrain.structure import FeedForwardNetwork


class NeuroSim():
    def __init__(self,NNet,visualization):
        self.numAgents = 1
        self.agents = []
        for x in range(0, self.numAgents):
            self.agents.append(NeuroAgent(NNet))
        self.frontierProducer = SimpleProducer()
        self.scorer = SimpleScorer()
        self.hotSpotFilter = SimpleHotspotFilter()
        self.fovFilter = SimpleFovFilter()
        self.visualization = visualization
        self.frontierController = FrontierController(self.scorer,self.frontierProducer,self.agents, [self.hotSpotFilter, self.fovFilter])

    def calcScore(self):
        i = 0
        visualizer = Visualizer()
        totalScore = 0
        iterations = 500
        if (self.visualization == 1):
            iterations = 1000


        while(i < iterations): #frontierController.hasData()):
            self.frontierController.tick()
            totalScore += self.agents[0].getScore()
            if (self.visualization == 1):
                bla = 1
                visualizer.vis(self.frontierController.frontierData, self.frontierController.agentLocations)
            i = i +1

        return totalScore
