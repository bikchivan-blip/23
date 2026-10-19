import random

n = int(input("Введіть кількість елементів: "))

a = []
for i in range(n):
    a.append(random.randint(1, 20))

print("Початковий список:", a)

s = sum(a)
sr = s / n
print("Середнє арифметичне:", sr)

mn = min(a)
print("Мінімальний елемент:", mn)

ind = [] 
for i in range(n):
    if a[i] % 2 != 0:
        a[i] = mn
        ind.append(i)

print("Змінений список:", a)
print("Індекси замінених елементів:", ind)