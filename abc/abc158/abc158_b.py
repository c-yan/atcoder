N, A, B = map(int, input().split())

result = 0
result += N // (A + B) * A
result += min(N % (A + B), A)
print(result)
