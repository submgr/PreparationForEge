Q = list(range(13, 40 + 1))
P = list(range(7, 25 + 1))

A = []

for x in range(1, 1000):
    if (((x in P) and (not(x in Q))) <= (x in A)) == False:
        A.append(x)

print(A)

# 7 = 7
# 12 = 12
# 12 - 7 = 5
# Ответ: 5
