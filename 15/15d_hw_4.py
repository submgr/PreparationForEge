Q = list(range(3, 10 + 1))
P = list(range(11, 17 + 1))

A = []

for x in range(1, 1000):
    if (((x in P) or (x in Q)) <= (x in A)) == False:
        A.append(x)
print(A)

#Ответ: 7!!

# НАС ПРОСЯТ ПОСЧИТАТЬ ТОЛЬКО ТОЧКИ С ЧЕТНЫМИ ЗНАЧЕНИЯМИ!! ВНИМАТЕЛЬНЕЙ