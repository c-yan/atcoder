N = int(input())
S = input()

print(sum(1 for i in range(N - 1) if S[i] != S[i + 1]) + 1)
