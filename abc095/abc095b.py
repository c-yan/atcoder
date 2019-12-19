N, X = map(int, input().split())
m = list(map(int, (input() for _ in range(N))))

print((X - sum(m)) // min(m) + N)
