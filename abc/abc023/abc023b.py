N = int(input())
S = input()

t = 'b'
for i in range(51):
    if S == t:
        print(i)
        exit()
    if i % 3 == 0:
        t = 'a' + t + 'c'
    elif i % 3 == 1:
        t = 'c' + t + 'a'
    elif i % 3 == 2:
        t = 'b' + t + 'b'
print(-1)
