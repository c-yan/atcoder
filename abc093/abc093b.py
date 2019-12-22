A, B, K = map(int, input().split())

for i in sorted(set(list(range(A, min(A + K, B + 1))) + list(range(B, max(B - K, A - 1), -1)))):
    print(i)
