from itertools import permutations

S1 = input()
S2 = input()
S3 = input()

s1 = [ord(c) - 97 for c in S1]
s2 = [ord(c) - 97 for c in S2]
s3 = [ord(c) - 97 for c in S3]

a = sorted(set(s1 + s2 + s3))
if len(a) > 10:
    print('UNSOLVABLE')
    exit()

if len(a) < 10:
    for i in range(30, 30 + (10 - len(a))):
        a.append(i)

b = [0] * 100
l = set([s1[0], s2[0], s3[0]])
for p in permutations(a):
    if p[0] in l:
        continue

    for i in range(10):
        b[p[i]] = chr(i + 48)

    N1 = int(''.join(b[c] for c in s1))
    N2 = int(''.join(b[c] for c in s2))
    N3 = int(''.join(b[c] for c in s3))

    if N1 + N2 == N3:
        print(N1)
        print(N2)
        print(N3)
        exit()
print('UNSOLVABLE')
