N = int(input())
s = input()
t = input()
if s == t:
    print(N)
else:
    for i in range(1, N + 1):
        if s[i:] == t[:-i]:
            break
    print(2 * N - (N - i))
