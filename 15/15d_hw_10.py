Q = list(range(18, 32 + 1))
P = list(range(5, 20 + 1))

A = list(range(1, 1000))

for x in range(1, 1000):
    if (((x in A) <= (x in P)) or (x in Q)) == False:
        A.remove(x)

print(A)

# 5 = 5
# 32 = 32
# 32 - 5 = 27
# ответ: 27