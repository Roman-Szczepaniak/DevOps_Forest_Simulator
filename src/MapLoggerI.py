from abc import ABC, abstractmethod

class MapLoggerI(ABC):
    @abstractmethod
    def log(self, map_grid):
        pass
