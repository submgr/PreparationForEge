Q = list(range(18, 41 + 1))
P = list(range(9, 17 + 1))
A = []
for x in range(1, 100):
    if (((x in P) or (x in Q)) <= (x in A)) == False:
        A.append(x)

print(A)

# 9 = 9
# 41 = 41
# 41 - 9 = 32
# ответ: 32