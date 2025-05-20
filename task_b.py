def обчислити_pn(n):

    if n < 1:
        raise ValueError("n має бути >= 1")
    
    результат = 1.0
    for i in range(1, n + 1):
        результат *= (i + 1) / i
    
    return результат

def головна():
    try:
        n = int(input("Введіть значення n (n >= 1): "))
        
        результат = обчислити_pn(n)
        print(f"P{n} = {результат}")
        
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    головна() 