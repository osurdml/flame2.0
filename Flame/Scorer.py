__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod

class Scorer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def calcScore(self,frontierConsumer, frontierData, workingNN): pass
    def getScore(self): pass
