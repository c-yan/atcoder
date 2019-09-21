n = int(input())
l = [int(e) for e in input().split()]
if max(l) < sum(l) - max(l):
    print('Yes')
else:
    print('No')
