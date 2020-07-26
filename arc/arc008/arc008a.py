N = int(input())

print(min((N + 9) // 10 * 100, N // 10 * 100 + N % 10 * 15))
