n = int(input())

if n == 1:
    print('BOWWOW')
    exit()

a = n * (n + 1) // 2
for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0:
        print('BOWWOW')
        break
else:
    print('WANWAN')
