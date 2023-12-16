N = int(input())
r = input()

t = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
print(sum(t[c] for c in r) / N)
