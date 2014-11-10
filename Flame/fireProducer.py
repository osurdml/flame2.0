__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod
import osgreo.gdal
import pygame
import sklearn.cluster


class FireProducer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getFireData(self): pass
# importing time of arrival and fire intensity.
        toa = osgeo.gdal.Open(toa_file).ReadAsArray()
        fli = osgeo.gdal.Open(fli_file).ReadAsArray()
#filter frontier

# Extract Clusters


    def hasData(self): pass

