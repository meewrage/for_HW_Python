# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

print("Введите сумму и произведение двух чисел")
s = int(input())
p = int(input())
for x in range(s+1):
    for y in range(p+1):
        if s == x + y and p == x * y:
            print(x, y)