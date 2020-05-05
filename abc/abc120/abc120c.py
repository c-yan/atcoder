S = input()

t = S.count('0')
print(2 * min(t, len(S) - t))
