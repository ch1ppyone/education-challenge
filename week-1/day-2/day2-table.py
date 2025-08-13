print("Таблцца умножения цикла for")
for i in range (1, 11):
    for j in  range (1, 11):
        print (f"{i} x {j}  = {i*j} ")


print("\nТаблцца умножения цикла while")
i = 1
while i<=10:
    j = 1
    while j<=10:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1