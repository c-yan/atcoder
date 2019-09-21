n = int(input())
s = [input() for _ in range(n)]
for i in range(n):
    s[i] = ''.join(sorted(s[i]))
t = {}
for i in range(n):
    if s[i] in t:
        t[s[i]] += 1
    else:
        t[s[i]] = 1
print(sum(t[k] * (t[k] - 1) // 2 for k in t))
