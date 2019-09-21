N, K = map(int, input().split())
D = list(map(int, input().split()))
d = list(map(str, D))
while True:
  if all(c not in d for c in str(N)):
    break
  N += 1
print(N)
