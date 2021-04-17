N = input()

for i in range(10):
    if N.find(str(i) * 3) == -1:
        continue
    print('Yes')
    break
else:
    print('No')
