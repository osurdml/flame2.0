from abc import ABCMeta, abstractmethod
from Filters import Filters
import math

class FovFilter(Filters):
        def __init__(self):
            self.state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.fov = 3000
            self.frontierCenter = [100,100]

        def filterData(self, frontierData, hotspotData, myLoc, agentLocations):

            self.state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for x in agentLocations:
                if self.calcDist(myLoc, x) < self.fov:

                    if (myLoc[0] -x[0]) == 0:
                        angle = 0
                    else:
                        angle = math.atan2((myLoc[1] - x[1]), (myLoc[0] - x[0]))

                    if (angle >= 0) and (angle < math.pi/2):
                        self.state[0] += 1
                        self.state[1] += self.calcDist(myLoc, x)
                    if (angle > math.pi/2) and (angle < math.pi):
                        self.state[2] += 1
                        self.state[3] += self.calcDist(myLoc, x)
                    if (angle > math.pi) and (angle < math.pi *3/2):
                        self.state[4] += 1
                        self.state[5] += self.calcDist(myLoc, x)
                    if (angle > math.pi *3/2) and (angle < math.pi *2):
                        self.state[6] += 1
                        self.state[7] += self.calcDist(myLoc, x)

            for x in hotspotData:
                if self.calcDist(myLoc, x) < self.fov:
                    if (myLoc[0] -x[0]) == 0:
                        angle = 0
                    else:
                        angle = math.atan2((myLoc[1] - x[1]), (myLoc[0] - x[0]))

                    if (angle >= 0) and (angle < math.pi/2):
                        self.state[8] += 1
                        self.state[9] += self.calcDist(myLoc, x)
                    if (angle > math.pi/2) and (angle < math.pi):
                        self.state[10] += 1
                        self.state[11] += self.calcDist(myLoc, x)
                    if (angle > math.pi) and (angle < math.pi *3/2):
                        self.state[12] += 1
                        self.state[13] += self.calcDist(myLoc, x)
                    if (angle > math.pi *3/2) and (angle < math.pi *2):
                        self.state[14] += 1
                        self.state[15] += self.calcDist(myLoc, x)

            self.state[16] = self.calcDist(myLoc, self.frontierCenter)

        def calcDist(self,a, b):
            distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
            return distance

        def getData(self):
            return self.state
