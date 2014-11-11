__author__ = 'Caleytown'

from FireConsumer import FireConsumer
from abc import ABCMeta, abstractmethod

class Agent(FireConsumer):
    __metaclass__ = ABCMeta

    @abstractmethod
    def updateScore(self): pass

    @abstractmethod
    def consumeFireData(self): pass
