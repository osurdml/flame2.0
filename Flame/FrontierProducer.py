__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod
import osgeo.gdal
#import pygame
#import sklearn.cluster

class FrontierProducer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def GetFrontierData(self, step): pass
    def hasData(self): pass

