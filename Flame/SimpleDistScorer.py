from Scorer import Scorer
from abc import ABCMeta, abstractmethod
from random import randint

class SimpleDistScorer(Scorer):

    def __init__(self):
        self.score = 0
        self.scoreCompare = 0
        self.globalScore = 0


    def calcScore(self,filterConsumers, hotspotFilterData, workingNN):
        flag = 0
        self.score = 0
        for hs in hotspotFilterData:
            closestAgentDist = 10000000
            for agent in filterConsumers:
                distSquared = (agent.getLocation()[0]-hs[0])**2+(agent.getLocation()[1]-hs[1])**2
                if(distSquared < closestAgentDist):
                    closestAgentDist = distSquared
            self.score += closestAgentDist

        self.globalScore = self.score
        #del filterConsumers[workingNN]
        #for hs in hotspotFilterData:
        #    closestAgentDist = 10000000
        #    for agent in filterConsumers:
        #        distSquared = (agent.getLocation()[0]-hs[0])**2+(agent.getLocation()[1]-hs[1])**2
        #        if(distSquared < closestAgentDist):
        #            closestAgentDist = distSquared
        #    self.score -= closestAgentDist

    def getScore(self):
        return self.score

    def getGlobalScore(self):
        return self.globalScore