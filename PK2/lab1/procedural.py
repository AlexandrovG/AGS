import sys
import math

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка! Введите число.")

def solve_biquadratic(a, b, c):
    if a == 0:
        print("Коэффициент A не может быть равен 0!")
        return []
    
    print(f"\nУравнение: {a}*x^4 + {b}*x^2 + {c} = 0")
    
    D = b**2 - 4*a*c
    print(f"Дискриминант D = {D}")
    
    roots = []
    
    if D < 0:
        print("Дискриминант отрицательный. Действительных корней нет.")
    elif D == 0:
        t = -b / (2*a)
        if t > 0:
            x1 = math.sqrt(t)
            x2 = -math.sqrt(t)
            roots = [x1, x2]
            print(f"Корни уравнения: x1 = {x1:.4f}, x2 = {x2:.4f}")
        elif t == 0:
            roots = [0]
            print("Корень уравнения: x = 0")
        else:
            print("Нет действительных корней.")
    else:
        t1 = (-b + math.sqrt(D)) / (2*a)
        t2 = (-b - math.sqrt(D)) / (2*a)
        
        if t1 > 0:
            x1 = math.sqrt(t1)
            x2 = -math.sqrt(t1)
            roots.extend([x1, x2])
        elif t1 == 0:
            roots.append(0)
        
        if t2 > 0:
            x3 = math.sqrt(t2)
            x4 = -math.sqrt(t2)
            if x3 not in roots and -x3 not in roots:
                roots.extend([x3, x4])
        elif t2 == 0 and 0 not in roots:
            roots.append(0)
        
        if roots:
            roots = list(set(roots))
            roots.sort()
            print(f"Найдено {len(roots)} действительных корней:")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} = {root:.4f}")
        else:
            print("Действительных корней нет.")
    
    return roots

def main():
    print("=" * 60)
    print("РЕШЕНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ: A*x^4 + B*x^2 + C = 0")
    print("=" * 60)
    
    a = b = c = None
    
    if len(sys.argv) >= 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
            print(f"Коэффициенты из командной строки: A={a}, B={b}, C={c}")
        except ValueError:
            print("Ошибка в аргументах. Будет выполнен ввод с клавиатуры.")
            a = b = c = None
    
    if a is None:
        print("\nВведите коэффициенты биквадратного уравнения:")
        a = get_valid_float("Коэффициент A (не равен 0): ")
        while a == 0:
            print("Коэффициент A не может быть равен 0!")
            a = get_valid_float("Коэффициент A (не равен 0): ")
    
    if b is None:
        b = get_valid_float("Коэффициент B: ")
    
    if c is None:
        c = get_valid_float("Коэффициент C: ")
    
    solve_biquadratic(a, b, c)

if __name__ == "__main__":
    main()