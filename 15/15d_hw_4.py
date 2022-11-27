Q = list(range(3, 10))
P = list(range(11, 17))

A = []

for x in range(1, 1000):
    if (((x in P) or (x in Q)) <= (x in A)) == False:
        A.append(x)
print(len(A))

#Ответ: 13