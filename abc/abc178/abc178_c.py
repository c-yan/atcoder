m = 1000000007

N = int(input())

print((pow(10, N, m) - pow(9, N, m) * 2 + pow(8, N, m)) % m)
