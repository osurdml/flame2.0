class 

def getFrontierData(self, step):
# importing time of arrival and fire intensity.
    self.toa = osgeo.gdal.Open(toa_file).ReadAsArray()
    self.char = osgeo.gdal.Open(fli_file).ReadAsArray() #characteristic, in this case fireline intensity
    burning = np.where(self.toa <= tick, self.fire_char, np.zeros_like(self.fire_char))
    return burning
def hasData(self):
    pass


