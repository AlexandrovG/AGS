from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    figure_type = "Прямоугольник"
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)
    
    def area(self):
        return self.width * self.height
    
    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            self.get_figure_type(),
            self.color.color,
            self.width,
            self.height,
            self.area()
        )