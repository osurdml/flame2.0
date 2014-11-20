from abc import ABCMeta, abstractmethod

class Filters():
   __metaclass__ = ABCMeta

   @abstractmethod
   def filterData(self, Data): pass

   @abstractmethod
   def getData(self): pass
