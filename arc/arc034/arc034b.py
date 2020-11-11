N = int(input())

def f(x):
    return sum(int(c) for c in str(x))

result = []
for i in range(1, 9 * len(str(N)) + 1):
    t = N - i
    if t < 0:
        break
    if t + f(t) == N:
        result.append(t)
print(len(result))
if len(result) != 0:
    print(*result[::-1], sep='\n')
