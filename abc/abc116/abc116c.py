N = int(input())
h = list(map(int, input().split()))

result = 0
while True:
    start = N
    for i in range(N):
        if h[i] != 0:
            start = i
            break
    if start == N:
        break
    end = N - 1
    count = float('inf')
    for i in range(start, N):
        if h[i] == 0:
            end = i - 1
            break
        if h[i] < count:
            count = h[i]
    for i in range(start, end + 1):
        h[i] -= count
    result += count
print(result)
