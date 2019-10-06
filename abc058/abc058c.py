n = int(input())

u = [float('inf')] * 26
for _ in range(n):
    S = input()
    t = [0] * 26
    for i in range(len(S)):
        t[ord(S[i]) - ord('a')] += 1
    for i in range(26):
        u[i] = min(u[i], t[i])
print(''.join(chr(i + ord('a')) * u[i] for i in range(26)))
