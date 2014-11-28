from Scorer import Scorer
from abc import ABCMeta, abstractmethod
from random import randint

class SimpleDistScorer(Scorer):

    def __init__(self):
        self.score = 0


    def calcScore(self,filterConsumers, hotspotFilterData):
        flag = 0
        self.score = 0
        if(abs(filterConsumers[0].getLocation()[0]-hotspotFilterData[0][0])+abs(filterConsumers[0].getLocation()[1]-hotspotFilterData[0][1]) <= 20):
            self.score = 0
        else:
            self.score = abs(filterConsumers[0].getLocation()[0]-hotspotFilterData[0][0])+abs(filterConsumers[0].getLocation()[1]-hotspotFilterData[0][1])








    def getScore(self):
        return self.score
