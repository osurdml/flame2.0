from abc import ABCMeta, abstractmethod
from Filters import Filters
import math

class FovFilter(Filters):
        def __init__(self):
            self.state = 0
            pass
        def filterData(self, frontierData, hotspotData, myLoc, agentLocations):
            print myLoc
            print agentLocations

            for x in agentLocations:
                if (myLoc[0] -x[0]) == 0:
                    angle = 0
                else:
                    angle = math.atan2((myLoc[1] - x[1]), (myLoc[0] - x[0]))

                if (angle >= 0) and (angle < math.pi/2):
                    self.state[0] += 1
                    self.state[4] += calcDist(myloc, x)
                    print angle
                if (angle > math.pi/2) and (angle < math.pi):
                    self.state[1] += 1
                    self.state[5] += calcDist(myloc, x)
                    print angle
                if (angle > math.pi) and (angle < math.pi *3/2):
                    self.state[2] += 1
                    self.state[6] += calcDist(myloc, x)
                    print angle
                if (angle > math.pi *3/2) and (angle < math.pi *2):
                    print angle
                    self.state[3] += 1
                    self.state[7] += calcDist(myloc, x)

            for x in hotspotData:
                if (myLoc[0] -x[0]) == 0:
                    angle = 0
                else:
                    angle = math.atan2((myLoc[1] - x[1]), (myLoc[0] - x[0]))

                if (angle >= 0) and (angle < math.pi/2):
                    self.state[8] += 1
                    self.state[12] += calcDist(myloc, x)
                    print angle
                if (angle > math.pi/2) and (angle < math.pi):
                    self.state[9] += 1
                    self.state[13] += calcDist(myloc, x)
                    print angle
                if (angle > math.pi) and (angle < math.pi *3/2):
                    self.state[10] += 1
                    self.state[14] += calcDist(myloc, x)
                    print angle
                if (angle > math.pi *3/2) and (angle < math.pi *2):
                    print angle
                    self.state[11] += 1
                    self.state[15] += calcDist(myloc, x)
            #self.state[16] = frontierCenter

        def calcDist(a, b):
            distance = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
            return distance

        def getData(self): 
            return self.state
