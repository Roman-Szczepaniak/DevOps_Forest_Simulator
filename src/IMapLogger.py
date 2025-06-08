from abc import ABC, abstractmethod

class IMapLogger(ABC):
    @abstractmethod
    def log(self, map_grid, title=None):
        pass
