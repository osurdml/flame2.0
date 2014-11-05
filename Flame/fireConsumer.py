__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod

class FireConsumer:


    @abstractmethod
    def updateScore(self): pass

    @abstractmethod
    def consumeFireData(self): pass