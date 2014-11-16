from abc import ABCMeta, abstractmethod

class FrontierConsumer():

    @abstractmethod
    def updateScore(self, scorer): pass

    @abstractmethod
    def consumeFrontierData(self, frontierData): pass
