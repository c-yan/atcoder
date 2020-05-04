from collections import deque

Q = int(input())

S = deque()
for _ in range(Q):
    Query = input().split()
    if Query[0] == '1':
        C = Query[1]
        X = int(Query[2])
        S.append((C, X))
    elif Query[0] == '2':
        D = int(Query[1])
        d = {}
        while D != 0 and len(S) != 0:
            C, X = S.popleft()
            d.setdefault(C, 0)
            if X >= D:
                d[C] += D
                if X != D:
                    S.appendleft((C, X - D))
                D = 0
            else:
                d[C] += X
                D -= X
        print(sum(v * v for v in d.values()))
