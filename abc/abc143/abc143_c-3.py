from itertools import groupby

N = int(input())
S = input()

print(len(list(groupby(S))))
