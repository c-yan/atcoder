N = input()
n = int(N)
t = n % 10 ** (len(N) - 1) + 1
print(max(sum(map(int, N)), sum(map(int, str(n - t)))))
