def обчислити_xk(x, k):
    
    if k < 1:
        raise ValueError("k має бути >= 1")
    
    return ((-1) ** k) * (x ** k) / k

def головна():
    try:
        x = float(input("Введіть значення x: "))
        k = int(input("Введіть значення k (k >= 1): "))
        
        результат = обчислити_xk(x, k)
        print(f"X{k} = {результат}")
        
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    головна() 