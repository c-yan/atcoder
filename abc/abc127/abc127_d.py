N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]

BC.sort(key=lambda x: x[1], reverse=True)
t = 0
for B, C in BC:
    A.extend([C] * B)
    t += B
    if t > N:
        break
A.sort(reverse=True)
print(sum(A[:N]))
