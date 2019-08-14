n = int(input())
t = 10 ** (len(str(n - 1)) - 1)
print(sum(int(e) for e in str(t)) + sum(int(e) for e in str(n - t)))
