N, A, B = map(int, input().split())

if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    print(min(A, N - B + 1) + (B - A - 1) // 2)
