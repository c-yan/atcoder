from collections import deque

def conv(i, j):
    return i * 1001 + j

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 10 ** 12

dp = [INF] * (1001 * 1001)

dp[0] = 0
q = deque([(0, 0)])
while q:
    i, j = q.popleft()

    if i >= N:
        dp[conv(N, M)] = min(dp[conv(N, M)], dp[conv(i, j)] + (M - j))
        continue

    if j >= M:
        dp[conv(N, M)] = min(dp[conv(N, M)], dp[conv(i, j)] + (N - i))
        continue

    if A[i] == B[j] and dp[conv(i + 1, j + 1)] > dp[conv(i, j)]:
        dp[conv(i + 1, j + 1)] = dp[conv(i, j)]
        q.append((i + 1, j + 1))
        continue

    if dp[conv(i + 1, j + 1)] > dp[conv(i, j)] + 1:
        dp[conv(i + 1, j + 1)] = dp[conv(i, j)] + 1
        q.append((i + 1, j + 1))

    if dp[conv(i + 1, j)] > dp[conv(i, j)] + 1:
        dp[conv(i + 1, j)] = dp[conv(i, j)] + 1
        q.append((i + 1, j))

    if dp[conv(i, j + 1)] > dp[conv(i, j)] + 1:
        dp[conv(i, j + 1)] = dp[conv(i, j)] + 1
        q.append((i, j + 1))
print(dp[conv(N, M)])
