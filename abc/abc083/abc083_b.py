N, A, B = map(int, input().split())

result = 0
for i in range(1, N + 1):
    if A <= sum(map(int, str(i))) <= B:
        result += i
print(result)
