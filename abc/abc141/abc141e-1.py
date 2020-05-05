# PyPy なら通る
N = int(input())
S = input()

result = 0
for i in range(N - 1, 0, -1):
    if i <= result:
        break
    t = 0
    for j in range(N - i):
        if S[j] == S[j+i]:
            t += 1
            if t > result:
                result = t
            if result == i:
                break
        else:
            t = 0

print(result)
