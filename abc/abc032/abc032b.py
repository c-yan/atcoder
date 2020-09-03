s = input()
k = int(input())

t = set()
for i in range(len(s) - k + 1):
    t.add(s[i:i + k])
print(len(t))
