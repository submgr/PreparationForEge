Q = list(range(18, 37 + 1))
P = list(range(2, 16 + 1))

A = []

for x in range(1, 1000):
    if (((x in P) or (x in Q)) <= (x in A)) == False:
        A.append(x)

print(A)

# 2 = 2
# 37 = 37
# 37 - 2 = 35
# Ответ: 35
