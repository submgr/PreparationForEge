Q = list(range(15, 39 + 1))
P = list(range(10, 17 + 1))
A = list(range(1, 1000))

for x in range(1, 1000):
    if (((x in Q) <= (x in P)) <= (not(x in A))) == False:
        A.remove(x)

print(A)

# 18 = 17
# 39 = 39
# 39 - 17 = 22
# Ответ: 22 