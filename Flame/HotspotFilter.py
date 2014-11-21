from abc import ABCMeta, abstractmethod
from Filters import Filters
import numpy as np
import Config
import sklearn.cluster
class HotspotFilter(Filters):

    def __init__(self):
        self.frontierData = 0
        self.hotspotloc = []
        self.HOTSPOT_MIN = Config.HOTSPOT_MIN
    def filterData(self, frontierData):
        self.frontierData = frontierData
        self.frontier = (self.frontierData >0).astype(np.uint8)
        convolve_row = self.frontier[1:-1,:] + self.frontier[:-2,:] + self.frontier[2:,:]
        convolve_col = convolve_row[:,1:-1] + convolve_row[:,:-2] + convolve_row[:,2:]
        self.frontier = np.logical_and(convolve_col <8, convolve_col > 0).nonzero()
        self.frontier_mask = np.zeros_like(self.frontierData)
        self.frontier_mask[self.frontier] = 1
        hotspots = np.where(self.frontierData > self.HOTSPOT_MIN, np.ones_like(self.frontierData), np.zeros_like(self.frontierData))
        hotspots = np.logical_and(hotspots, self.frontier_mask)
        if hotspots.shape[0] > 2:
            k = int(np.sqrt(hotspots.shape[0]/2))
            self.kmeans = sklearn.cluster.KMeans(n_clusters = k)
            self.kmeans.fit(hotspots)
            self.hotspotloc = self.kmeans.cluster_centers_
    def getData(self):
        return self.hotspotloc
