N = int(input())
S1 = input()
S2 = input()

m = 1000000007

if S1[0] == S2[0]:
    result = 3
else:
    result = 6
x = 0
W = len(S1)
while x < W:
    if S1[x] == S2[x]:
        if x + 1 == W:
            break
        result *= 2
        result %= m
        x += 1
    else:
        if x + 2 == W:
            break
        if S1[x + 2] != S2[x + 2]:
            result *= 3
            result %= m
        x += 2
print(result)
