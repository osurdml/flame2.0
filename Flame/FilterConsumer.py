from abc import ABCMeta, abstractmethod

class FilterConsumer():
    @abstractmethod
    def consumeFilterData(self, data):
        pass
    def getLocation(self):
        pass
