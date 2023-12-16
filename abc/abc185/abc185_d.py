N, M, *A = map(int, open(0).read().split())

if M == 0:
    print(1)
    exit()

A.sort()
p = 0
intervals = []
for a in A:
    t = a - p - 1
    if t != 0:
        intervals.append(t)
    p = a
t = N - A[-1]
if t != 0:
    intervals.append(t)
if len(intervals) == 0:
    print(0)
    exit()
k = max(min(intervals), 1)

result = 0
for x in intervals:
    result += (x + k - 1) // k
print(result)
