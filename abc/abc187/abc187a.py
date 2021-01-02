def S(n):
    return sum(int(c) for c in str(n))


A, B = map(int, input().split())

print(max(S(A), S(B)))
