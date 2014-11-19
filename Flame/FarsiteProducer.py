from FrontierProducer import FrontierProducer
import osgeo.gdal
import numpy as np
from abc import ABCMeta, abstractmethod

class FarsiteProducer(FrontierProducer):
    def __init__(self):
        # importing time of arrival and fire intensity.
        toa_file = "ash1_raster.toa"
        fli_file = "ash1_raster.fli"
        self.toa = osgeo.gdal.Open(toa_file).ReadAsArray()
        self.char = osgeo.gdal.Open(fli_file).ReadAsArray() #characteristic, in this case fireline intensity

    def getFrontierData(self, step):
        burning = np.where(self.toa <= step, self.char, np.zeros_like(self.char))
        return burning
    def hasData(self):
        pass


