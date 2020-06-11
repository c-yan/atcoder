S = input()

t = {'Left': '<', 'Right': '>', 'AtCoder': 'A'}
print(' '.join(t[s] for s in S.split()))
