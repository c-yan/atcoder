S = input()

S = S[::-1]
result = 0
t = [0] * 2019
m = 1
n = 0
for i in range(len(S)):
    t[n] += 1
    n += int(S[i]) * m
    n %= 2019
    result += t[n]
    m *= 10
    m %= 2019
print(result)
