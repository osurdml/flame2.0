__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod

class FrontierConsumer():


    @abstractmethod
    def updateScore(self, scorer): pass

    @abstractmethod
    def consumeFireData(self, fireData): pass
