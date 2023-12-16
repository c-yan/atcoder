def l2s(list, alphabets):
    return ''.join(alphabets[i] for i in list)


s = input()
K = int(input())

alphabets = sorted(set(s))
if K == 1:
    print(alphabets[0])
    exit()

j = 1
list = [0, 0]
while True:
    t = l2s(list, alphabets)
    if s.find(t) != -1:
        j += 1
        if K == j:
            print(t)
            exit()
        list.append(0)
    else:
        list[-1] += 1
        while list[-1] == len(alphabets):
            list.pop()
            list[-1] += 1
