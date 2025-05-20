import numpy as np

def обчислити_визначник(n, x):
    
    if n < 1:
        raise ValueError("n має бути >= 1")
    
    # Создаем матрицу
    матриця = np.zeros((n, n))
    
    # Заполняем диагональные элементы
    for i in range(n):
        матриця[i, i] = 1 + x**2
    
    # Заполняем элементы над и под главной диагональю
    for i in range(n-1):
        матриця[i, i+1] = x
        матриця[i+1, i] = x
    
    # Вычисляем определитель
    return np.linalg.det(матриця)

def головна():
    try:
        n = int(input("Введіть порядок визначника n (n >= 1): "))
        x = float(input("Введіть значення x: "))
        
        результат = обчислити_визначник(n, x)
        print(f"Визначник порядку {n} = {результат}")
        
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    головна() 