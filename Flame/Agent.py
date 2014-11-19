from abc import ABCMeta, abstractmethod

class Agent():
    __metaclass__ = ABCMeta

    @abstractmethod
    def updateScore(self): pass

    @abstractmethod
    def consumeFilterData(self, FilterData): pass

    @abstractmethod
    def getLocation(self):
        pass
