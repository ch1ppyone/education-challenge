
try:
    a = int(input())
    b= int(input())
except ValueError:
    print("Ввод должен быть числом")
    exit()

total= a+b
diff = a-b
prod = a*b
power = a**b 
sqrta = a**0.5

print(f"Сумма: {total}")
print(f"Разность: {diff}")
print(f"Произведение: {prod}")
print(f"Степень: {power}")
print(f"Квадратный корень: {sqrta}")


if b==0:
    print(f"Делить на ноль нельзя!")
else:
    div = a/b  
    print( f"Деление: {div}")