from sys import exit

A, B, X = map(int, input().split())


def is_ok(N):
    return A * N + B * len(str(N)) <= X


if is_ok(10 ** 9):
    print(10 ** 9)
    exit()

if not is_ok(1):
    print(0)
    exit()

N = 10 ** 9
while not is_ok(N):
    N //= 10

result = min((X - B * len(str(N))) // A, N * 10 - 1)
print(result)
