N = int(input())
a = list(map(int, input().split()))
for i, _ in sorted(enumerate(a), key = lambda x: x[1], reverse = True):
  print(i + 1)
