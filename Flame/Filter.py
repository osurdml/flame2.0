from abc import ABCMeta, abstractmethod

class Filter():
   __metaclass__ = ABCMeta

   @abstractmethod
   def filterData(self): pass

   @abstractmethod
   def consumeData(): pass
