X = input()

result = 0
t = 0
for i in range(len(X)):
    if X[i] == 'S':
        t += 1
    else:
        if t != 0:
            result += 2
            t -= 1
print(len(X) - result)
