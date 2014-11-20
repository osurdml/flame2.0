from Scorer import Scorer
from abc import ABCMeta, abstractmethod
from random import randint

class NeuroScorer(Scorer):

    def __init__(self):
        someNumber = 0


    def calcScore(self,fireConsumers, fireData):
        for k in fireConsumers:
            location = k.getLocation()
            self.isHotspotObserved(location)
            k.updateScore(location)

    def isHotspotObserved(self,agentLocation):
        return "noIdea"