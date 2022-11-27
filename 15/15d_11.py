R = list(range(12, 31 + 1))
Q = list(range(6, 15 + 1))
P = list(range(17, 23 + 1))
A = []

for x in range(1, 100):
    if (((x in A) or (x in P)) or ((x in Q) <= (x in R))) == False:
        A.append(x)

print(A)

# 6 = 6
# 11 = 12
# 12 - 6 = 6
# ответ: 6