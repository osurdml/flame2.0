__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod

class Displayer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self): pass