s = input()
t = len([c for c in s if c == '0'])
print(2 * min(t, len(s) - t))
