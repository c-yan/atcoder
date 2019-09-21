s = input()
k = int(input())
for i in range(len(s)):
    if s[i] == '1':
        k -= 1
        if k == 0:
            print(s[i])
            break
    else:
        print(s[i])
        break
