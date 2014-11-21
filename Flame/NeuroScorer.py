from Scorer import Scorer
from abc import ABCMeta, abstractmethod
from random import randint

class NeuroScorer(Scorer):

    def __init__(self):
        self.score = 0


    def calcScore(self,filterConsumers, hotspotFilterData):
        for x in filterConsumers:
            for y in hotspotFilterData:
                if(abs(x.getLocation[0]-y[0]+x.getLocation[1]-y[1]) > 20):
                    self.score += 1


    def getScore(self):
        return self.score