from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @classmethod
    def get_figure_type(cls):
        return cls.figure_type