A, B, C = map(int, input().split())

print(pow(A, pow(B, C, 4) + 4) % 10)
