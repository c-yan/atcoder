# しゃくとり法
N = int(input())
A = list(map(int, input().split()))

result = 0
r = 0
xs = A[0]
cs = A[0]
for l in range(N):
    while r < N - 1 and xs ^ A[r + 1] == cs + A[r + 1]:
        r += 1
        xs ^= A[r]
        cs += A[r]
    result += r - l + 1
    xs ^= A[l]
    cs -= A[l]
print(result)
