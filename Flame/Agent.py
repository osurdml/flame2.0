from FrontierConsumer import FrontierConsumer
from abc import ABCMeta, abstractmethod

class Agent(FrontierConsumer):
    __metaclass__ = ABCMeta

    @abstractmethod
    def updateScore(self): pass

    @abstractmethod
    def consumeFrontierData(self, FrontierData): pass
