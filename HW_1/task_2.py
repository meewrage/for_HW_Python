# Найти сумму числе трехзначного числа.
print("Введите трехзначное число", end=" :")
n = int(input())
if 99 < n < 1000:
    count = 0
    while n > 0:
        d = n % 10
        count += d
        n //= 10
    print("Сумма цифр равна", count)
else:
    print("Неверные данные") 