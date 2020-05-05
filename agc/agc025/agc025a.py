N = int(input())

t = 10 ** (len(str(N - 1)) - 1)
print(sum(int(e) for e in str(t)) + sum(int(e) for e in str(N - t)))
