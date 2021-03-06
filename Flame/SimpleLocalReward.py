from Scorer import Scorer
from abc import ABCMeta, abstractmethod
from random import randint

class SimpleLocalReward(Scorer):

    def __init__(self):
        self.score = 0
        self.scoreCompare = 0
        self.globalScore = 0


    def calcScore(self,filterConsumers, hotspotFilterData, workingNN):
        flag = 0
        self.score = 0
        self.globalScore = 0
        for agent in filterConsumers:
            closestAgentDist = 1000000000
            for hs in hotspotFilterData:
                distSquared = (agent.getLocation()[0]-hs[0])**2+(agent.getLocation()[1]-hs[1])**2
                if(distSquared < closestAgentDist):
                    closestAgentDist = distSquared
            self.score += closestAgentDist


        for hs in hotspotFilterData:
            closestAgentDist = 1000000000
            for agent in filterConsumers:
                distSquared = (agent.getLocation()[0]-hs[0])**2+(agent.getLocation()[1]-hs[1])**2
                if(distSquared < closestAgentDist):
                    closestAgentDist = distSquared
            self.globalScore += closestAgentDist

    def getScore(self):
        return self.score

    def getGlobalScore(self):
        return self.globalScore