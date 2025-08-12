num = int(input("Введите число: "))
print(f"Число: { num} ")
print(f"Квадрат: {num**2} ")

if num>=0:
    print(f"Квадратный корень: {num**0.5} ")
else:
    print(f"Квадратный корень: нет действительного корня")

if num % 2 == 0:
    print(f"Чётность: чётное") 
else:
    print(f"Чётность: нечётное")


if abs(num) >= 100 and abs(num) <= 999:
    a = num//100
    b = (num//10) % 10
    c = num % 10
    sum  = a + b + c
    print(f"Сумма цифр: {sum}")

else:
        print(f"Сумма цифр: не трёхзначное")
        exit()
