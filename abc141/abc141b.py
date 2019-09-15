S = input()
if all(c in 'RUD' for c in S[::2]) and all(c in 'LUD' for c in S[1::2]):
  print('Yes')
else:
  print('No')
