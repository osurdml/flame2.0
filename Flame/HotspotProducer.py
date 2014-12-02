from HotspotFilter import HotspotFilter
from FarsiteProducer import FarsiteProducer

step = 0
iterations = 500
fP = FarsiteProducer() 
hF = HotspotFilter()
hotspotLoc = []

def tick(step):
    frontierData = fP.getFrontierData(step)
    hotspotFilter = hF.filterData(frontierData)
    print hF.getData()
    print step
    hotspotLoc[step] = hF.getData()
    with open('hotspotLoc.pkl','wb') as output:
        pickle.dump(hotspotLoc,output,pickle.HIGHEST_PROTOCOL)

while step < iterations:
    tick(step)
    step = step + 1
