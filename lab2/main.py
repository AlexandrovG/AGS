from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

try:
    import numpy as np
    numpy_available = True
except ImportError:
    numpy_available = False
    print("Numpy не установлен. Установите: pip install numpy")

def main():
    N = 5
    
    print("Лабораторная работа №2. Объектно-ориентированные возможности Python")
    print("=" * 70)
    
    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")
    
    print(rectangle)
    print(circle)
    print(square)
    
    if numpy_available:
        print("\n" + "=" * 70)
        print("Демонстрация работы внешнего пакета (numpy):")
        
        arr = np.array([1, 2, 3, 4, 5])
        print(f"Создан массив numpy: {arr}")
        print(f"Среднее значение: {np.mean(arr)}")
        print(f"Стандартное отклонение: {np.std(arr):.2f}")
    else:
        print("\n" + "=" * 70)
        print("Для демонстрации внешнего пакета установите numpy: pip install numpy")

if __name__ == "__main__":
    main()