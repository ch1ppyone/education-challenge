num = int(input())
sum = 0

if num > 0:
    for i in range (1, num +1):
        if(i%2==0):
            sum +=i
    print(f"Сумма всех четных чисел от 1 до {num} = {sum}")

 
