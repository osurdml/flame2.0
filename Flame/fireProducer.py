__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod

class FireProducer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getFireData(self): pass

    def hasData(self): pass