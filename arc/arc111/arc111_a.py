N, M = map(int, input().split())

print(pow(10, N, M * M) // M % M)
