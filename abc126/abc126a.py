n, k = [int(e) for e in input().split()]
s = input()
print(s[:k - 1] + s[k - 1].lower() + s[k:])
