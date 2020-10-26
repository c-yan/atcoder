N = int(input())

divisors = set()
for i in range(1, int(N ** 0.5) + 1):
    if N % i != 0:
        continue
    divisors.add(i)
    divisors.add(N // i)

t = N * 2 - sum(divisors)
if t == 0:
    print('Perfect')
elif t > 0:
    print('Deficient')
elif t < 0:
    print('Abundant')
