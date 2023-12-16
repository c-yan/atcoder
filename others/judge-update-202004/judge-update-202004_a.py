S, L, R = map(int, input().split())

if L <= S <= R:
    print(S)
elif S < L:
    print(L)
elif S > R:
    print(R)
