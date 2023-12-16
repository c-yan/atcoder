A, B = map(int, input().split())

result = []
if A >= B:
    result.extend(range(1, A + 1))
    result.extend(-x for x in range(1, B))
    result.append(-sum(result))
else:
    result.extend(-x for x in range(1, B + 1))
    result.extend(range(1, A))
    result.append(-sum(result))
print(*result)
