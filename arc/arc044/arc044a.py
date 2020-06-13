N = int(input())


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_pseudo_prime(n):
    return (n % 2 != 0) and (n % 5 != 0) and (n % 3 != 0)


if N == 1:
    print('Not Prime')
elif is_prime(N) or is_pseudo_prime(N):
    print('Prime')
else:
    print('Not Prime')
