from Scorer import Scorer
from abc import ABCMeta, abstractmethod
from random import randint

class NeuroScorer(Scorer):

    def __init__(self):
        self.score = 0


    def calcScore(self,filterConsumers, hotspotFilterData):
        hotspotFilterData = [(200, 200)]
        flag = 0
        for y in hotspotFilterData:
           flag = 0
           for x in filterConsumers:
               if(abs(x.getLocation()[0]-y[0]+x.getLocation()[1]-y[1]) <= 20):
                   flag = 1
           if(flag == 0):
                self.score += 1

    def getScore(self):
        return self.score
