s = input()
t = s.count('0')
print(2 * min(t, len(s) - t))
