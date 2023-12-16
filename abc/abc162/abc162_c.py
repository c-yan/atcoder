def main():
    from math import gcd

    K = int(input())

    result = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            t = gcd(a, b)
            for c in range(1, K + 1):
                result += gcd(t, c)
    print(result)


main()
