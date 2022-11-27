Q = list(range(45, 88 + 1))
P = list(range(10, 57 + 1))

A = list(range(1, 10000))

for x in range(1, 10000):
    if (((x in P) <= (not(x in Q))) <= (not(x in A))) == False:
        A.remove(x)

print(A)

# 45 = 45
# 57 = 57
# 57 - 45 = 12
# Ответ: 12