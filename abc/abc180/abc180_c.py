N = int(input())

result = set()
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        result.add(i)
        result.add(N // i)
print(*sorted(result), sep='\n')
