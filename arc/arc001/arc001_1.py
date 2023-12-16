N = int(input())
c = input()

t = {'1': 0, '2': 0, '3': 0, '4': 0}
for e in c:
    t[e] += 1
print(max(t.values()), min(t.values()))
