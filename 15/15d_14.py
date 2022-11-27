Q = list(range(12, 32 + 1))
P = list(range(4, 13 + 1))

A = list(range(1, 10000))

for x in range(1, 10000):
    if (((x in A) <= (x in P)) or (x in Q)) == False:
        A.remove(x)

print(A)

# 4 = 4
# 32 = 32
# 32 - 4 = 28
# Ответ: 28