S = input()
K = int(input())

for i in range(len(S)):
    if S[i] == '1':
        K -= 1
        if K == 0:
            print(S[i])
            break
    else:
        print(S[i])
        break
