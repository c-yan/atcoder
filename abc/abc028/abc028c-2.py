ABCDE = list(map(int, input().split()))

t = []
for i in range(3):
  for j in range(i + 1, 4):
    for k in range(j + 1, 5):
      t.append(ABCDE[i] + ABCDE[j] + ABCDE[k])
t.sort()
print(t[-3])
