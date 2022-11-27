Q = list(range(18, 41 + 1))
P = list(range(15, 20 + 1))

A = []
for x in range(1, 1000):
    if (((not(x in A)) and (x in Q)) <= (x in P)) == False:
        A.append(x)

print(A)

# 21 = 20
# 41 = 41
# 41 - 20 = 21
# ответ: 21