S = input()

t = ''.join(c if c in 'ACGT' else ' ' for c in S)
print(max(map(len, t.split(' '))))
