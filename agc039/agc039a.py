S = input()
K = int(input())

t = bytearray(S * 3, 'us-ascii')
for i in range(1, len(t)):
    if t[i - 1] == t[i]:
        t[i] = 0
b0 = t[:len(S)].count(0)
b1 = t[len(S):len(S) * 2].count(0)
b2 = t[len(S) * 2:len(S) * 3].count(0)
print(b0 + b1 * (K // 2) + b2 * ((K - 1) // 2))
