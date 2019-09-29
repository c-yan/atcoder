N = int(input())
A = list(map(int, input().split()))

negatives = len([a for a in A if a < 0])
if negatives % 2 == 0:
    m = 0
else:
    m = min(abs(a) for a in A)
print(sum(abs(a) for a in A) - 2 * m)
