from abc import ABCMeta, abstractmethod
from Filters import Filters

class SimpleHotspotFilter(Filters):

    def __init__(self):
        self.hotspots = []
    def filterData(self, frontierData):
        self.hotspots = frontierData
    def getData(self):
        return self.hotspots
