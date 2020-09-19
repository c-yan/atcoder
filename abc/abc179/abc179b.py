N = int(input())

t = 0
max_run_length = 0
for _ in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        t += 1
    else:
        t = 0
    max_run_length = max(max_run_length, t)

if max_run_length >= 3:
    print('Yes')
else:
    print('No')
