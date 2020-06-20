N = int(input())
A = list(map(int, input().split()))

m = 1000000007

result = 1
t = [0, 0, 0]
for i in range(N):
    a = A[i]
    f = -1
    k = 0
    for j in range(3):
        if t[j] == a:
            k += 1
            if f == -1:
                t[j] += 1
                f = j
    result *= k
    result %= m
print(result)
