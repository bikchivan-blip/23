t = (5, 8, 3, 12, 7, 4, 9, 2)
print("Початковий кортеж:", t)

mn = min(t)
print("Мінімальний елемент:", mn)

res = ()

for i in range(len(t)):
    if t[i] % 2 != 0 and i % 2 == 0:
        res = res + (mn,)
    else:
        res = res + (t[i],)

print("Новий кортеж:", res)