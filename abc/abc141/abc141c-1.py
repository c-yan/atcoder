N, K, Q, *A = map(int, open(0).read().split())

score = [K - Q] * N
for a in A:
    score[a - 1] += 1

result = []
for i in range(N):
    if score[i] > 0:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
