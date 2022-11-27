Q = list(range(29, 88 + 1))
P = list(range(10, 55 + 1))

A = list(range(1, 1000))

for x in range(1, 1000):
    if (((x in P) <= (not(x in Q))) <= (not(x in A))) == False:
        A.remove(x)

print(A)

# 29 = 29
# 55 = 55

print("==========\nОтвет:")
print(55 - 29)

#Ответ: 26