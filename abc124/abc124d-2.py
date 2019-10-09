# 累積和
from sys import exit

N, K = map(int, input().split())
S = input()

p = '1'
count = 0
cs = []
for c in S:
    if c != p:
        cs.append(count)
        p = c
        count = 1
    else:
        count += 1
cs.append(count)
if p != '1':
    cs.append(0)

if len(cs) < 2 * K:
    print(N)
    exit()

for i in range(1, len(cs)):
    cs[i] += cs[i - 1]

result = cs[2 * K]
for i in range(2, len(cs) - 2 * K, 2):
    if cs[2 * K + i] - cs[i - 1] > result:
        result = cs[2 * K + i] - cs[i - 1]
print(result)
