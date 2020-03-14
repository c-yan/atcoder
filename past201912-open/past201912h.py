N = int(input())
C = list(map(int, input().split()))
Q = int(input())

all_min = min(C)
odd_min = min(C[::2])
all_sale = 0
odd_sale = 0
ind_sale = 0
for _ in range(Q):
    S = input()
    if S[0] == '1':
        _, x, a = map(int, S.split())
        t = C[x - 1] - all_sale - a
        if x % 2 == 1:
            t -= odd_sale
        if t >= 0:
            ind_sale += a
            C[x - 1] -= a
            all_min = min(all_min, t)
            if x % 2 == 1:
                odd_min = min(odd_min, t)
    elif S[0] == '2':
        _, a = map(int, S.split())
        if odd_min >= a:
            odd_sale += a
            odd_min -= a
            all_min = min(odd_min, all_min)
    elif S[0] == '3':
        _, a = map(int, S.split())
        if all_min >= a:
            all_sale += a
            all_min -= a
            odd_min -= a
print(all_sale * N + odd_sale * ((N + 1) // 2) + ind_sale)
