import random

n = 10

m = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(1, 50))
    m.append(row)

print("Початкова матриця:")
for row in m:
    print(row)

k = 0
for i in range(n):
    for j in range(n):
        if m[i][j] % 2 != 0:
            k = k + 1

print("\n1. Кількість непарних елементів:", k)

for i in range(n):
    for j in range(n):
        if i > j:
            m[i][j] = k

print("\n2. Матриця після заміни:")
for row in m:
    print(row)

for i in range(n):
    m[i].reverse()

print("\n3. Матриця після повороту:")
for row in m:
    print(row)