S = input()

t = []
start = -1
for i in range(len(S)):
    if S[i].isupper():
        if start == -1:
            start = i
        else:
            t.append(S[start:i+1])
            start = -1
t.sort(key=str.lower)
print(''.join(t))
