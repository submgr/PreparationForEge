Q = list(range(20, 30 + 1))
P = list(range(15, 55 + 1))
A = []
for x in range(1, 1000):
    if ((not(x in A)) <= (not((x in P) and not(x in Q)))) == False:
        A.append(x)

print(A)

# 15 = 15
# 55 = 55
# 55 - 15 = 40
# ответ: 40