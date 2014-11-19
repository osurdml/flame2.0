from abc import ABCMeta, abstractmethod

class FrontierConsumer():

    @abstractmethod
    def consumeFrontierData(self, frontierData): pass
