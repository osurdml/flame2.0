__author__ = 'Caleytown'
from abc import ABCMeta, abstractmethod
import osgeo.gdal
import pygame
import sklearn.cluster


class FireProducer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getFireData(self, tick): 
# importing time of arrival and fire intensity.
        self.toa = osgeo.gdal.Open(toa_file).ReadAsArray()
        self.char = osgeo.gdal.Open(fli_file).ReadAsArray() #characteristic, in this case fireline intensity
        
        burning = np.where(self.toa <= tick, self.fire_char, np.zeros_like(self.fire_char))


    def hasData(self): pass

