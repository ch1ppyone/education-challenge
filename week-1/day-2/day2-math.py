end = False

while not end:
    command = int(input("Введите команду"))
    if command == 1:
        print("Решение линейного уравнения ax + b = 0")
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        if a != 0:
            x = -b / a
            print(f"Решение: x = {x}")
        else:
             if b == 0:
                 print("Бесконечно много решений")
             else:
                  print("Решений нет")

    elif command == 2:
        print("Нахождение максимума трех чисел")
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        c = float(input("Введите третье число: "))
        maximum = a
        if b > maximum:
            maximum = b
        if c > maximum:
            maximum = c
        
        print(f"Максимальное число: {maximum}")
    
    elif command == 3:
        print("Генерация арифметической прогрессии")
        i = int(input("Введите начальное значение: "))
        step = int(input("Введите шаг: "))
        n = int(input("Введите количество элементов: "))

        current = i
        for _ in range(n):
            print(current, end=' ')
            current += step
        print()

    elif command == 4:
        print("Генерация геометрической прогрессии")
        i = int(input("Введите начальное значение: "))
        step = int(input("Введите шаг: "))
        n = int(input("Введите количество элементов: "))

        current = i
        for _ in range(n):
            print(current, end=' ')
            current *= step
        print()
    else:
        print("Неверная команда. Выход из программы?")
        yn  = input("")
        if yn == 'y':
            end = True
            print("До свидания!")  
        else:
            continue


             
        