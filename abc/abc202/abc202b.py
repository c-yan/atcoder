S = input()

d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
print(''.join(d[c] for c in reversed(S)))
