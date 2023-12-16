N = int(input())
ST = []
for _ in range(N):
    S, T = input().split()
    ST.append((int(T), S))

ST.sort(reverse=True)
print(ST[1][1])
