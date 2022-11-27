Q = list(range(21, 91 + 1))
P = list(range(10, 51 + 1))
A = []
for x in range(1, 100):
    if (((x in P) and (x in Q)) <= (x in A)) == False:
        A.append(x)

print(A)

# 21 = 21
# 51 = 51
# 51 - 21 = 30
# ответ: 30