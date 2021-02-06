def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_pseudo_prime(n):
    if n == 1:
        return False
    return (n % 2 != 0) and (n % 5 != 0) and (n % 3 != 0)


N = int(input())

if is_prime(N) or is_pseudo_prime(N):
    print('Prime')
else:
    print('Not Prime')
