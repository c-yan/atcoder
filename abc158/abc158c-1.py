A, B = map(int, input().split())

result = -1
for i in range(2000):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        result = i
        break
print(result)
