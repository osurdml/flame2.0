__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod
import osgeo.gdal
#import pygame
#import sklearn.cluster

class FrontierProducer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def getFrontierData(self, step): pass
    def hasData(self): pass

