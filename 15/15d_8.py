Q = list(range(11, 64 + 1))
P = list(range(4, 32 + 1))
A = []
for x in range(1, 100):
    if ((x in A) or ((not(x in P)) <= (not(x in Q)))) == False:
        A.append(x)

print(A)

# 33 = 32
# 64 = 64
# 64 - 32 = 32
# ответ: 32