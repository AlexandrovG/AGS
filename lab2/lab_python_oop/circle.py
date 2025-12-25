from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math

class Circle(Figure):
    figure_type = "Круг"
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {:.2f}.'.format(
            self.get_figure_type(),
            self.color.color,
            self.radius,
            self.area()
        )