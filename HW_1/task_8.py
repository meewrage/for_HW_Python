# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
print("Введите размер шоколадки и сколько долек отрезать, а я скажу можно ли с помощью одного разреза так сделать: ")
m, n, k = int(input()),int(input()),int(input())
if (m > 1 or n > 1) and ( m <=  k < m * n or n <= k < m * n) and (k % m == 0 or k % n == 0) :
    print("yes")
else:
    print("no")