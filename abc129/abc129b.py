n = int(input())
w = [int(e) for e in input().split()]
result = float('inf')
for t in range(n -1):
  sd = abs(sum(w[0:t + 1]) - sum(w[t + 1:]))
  result = min(sd, result)
print(result)
