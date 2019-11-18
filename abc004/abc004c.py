N = int(input())

N %= 30
t = [1, 2, 3, 4, 5, 6]
for i in range(N):
    t[i % 5], t[i % 5 + 1] = t[i % 5 + 1], t[i % 5]
print(''.join(str(i) for i in t))
