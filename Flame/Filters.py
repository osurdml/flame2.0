from abc import ABCMeta, abstractmethod

class Filters():
   __metaclass__ = ABCMeta

   @abstractmethod
   def filterData(self): pass

   @abstractmethod
   def getData(): pass
