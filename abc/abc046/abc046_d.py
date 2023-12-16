s = input()

print(max((s.count('g') * 2 - len(s)) // 2, 0))
