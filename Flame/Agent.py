from abc import ABCMeta, abstractmethod
from FilterConsumer import FilterConsumer


class Agent(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def updateScore(self, score): pass

    @abstractmethod
    def consumeFilterData(self, FilterData): pass

    @abstractmethod
    def takeAction(self):pass

    @abstractmethod
    def getLocation(self):pass

    @abstractmethod
    def setTime(self):pass
