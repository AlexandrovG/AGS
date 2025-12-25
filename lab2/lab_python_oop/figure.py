from abc import ABC, abstractmethod

class Figure(ABC):
    figure_type = "Фигура"
    
    @abstractmethod
    def area(self):
        """Абстрактный метод для вычисления площади"""
        pass
    
    @classmethod
    def get_figure_type(cls):
        return cls.figure_type