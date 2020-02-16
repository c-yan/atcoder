N = int(input())

d1 = {}
for _ in range(N):
    S = input()
    if S in d1:
        d1[S] += 1
    else:
        d1[S] = 1

d2 = {}
for key in d1:
    value = d1[key]
    if value in d2:
        d2[value].append(key)
    else:
        d2[value] = [key]

key = sorted(d2.keys(), reverse=True)[0]
for s in sorted(d2[key]):
    print(s)
