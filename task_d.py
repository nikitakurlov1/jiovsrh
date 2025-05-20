def обчислити_ak(k):
   
    if k == 1 or k == 2:
        return 1
    
    # Используем рекурсию для вычисления ak
    return обчислити_ak(k-1) + обчислити_ak(k-2)

def обчислити_sn(n):
   
    if n < 1:
        raise ValueError("n має бути >= 1")
    
    результат = 0.0
    for k in range(1, n + 1):
        результат += обчислити_ak(k) / k
    
    return результат

def головна():
    try:
        n = int(input("Введіть значення n (n >= 1): "))
        
        результат = обчислити_sn(n)
        print(f"S{n} = {результат}")
        
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    головна() 