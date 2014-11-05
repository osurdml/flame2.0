__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod

class Scorer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def calcScore(self,fireConsumer, fireData): pass