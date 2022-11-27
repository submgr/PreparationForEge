Q = list(range(20, 105 + 1))
P = list(range(55, 80 + 1))
A = []
for x in range(1, 1000):
    if ((x in Q) <= (((x in P) == (x in Q)) or ((not(x in P)) <= (x in A)))) == False:
        A.append(x)

print(A)

# 1 = 1
# 20 = 20
# 20 - 1 = 19
# ответ: 19