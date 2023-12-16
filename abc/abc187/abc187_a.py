def S(n):
    result = 0
    while n != 0:
        result += n % 10
        n //= 10
    return result


A, B = map(int, input().split())

print(max(S(A), S(B)))
