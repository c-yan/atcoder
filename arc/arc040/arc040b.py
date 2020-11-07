N, R = map(int, input().split())
S = input()

result = 0
result += max(S.rfind('.') - (R - 1), 0)

t = N
while True:
    t = S.rfind('.', 0, t)
    if t == -1:
        break
    result += 1
    t = max(t - (R - 1), 0)

print(result)
