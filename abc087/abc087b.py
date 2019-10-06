A = int(input())
B = int(input())
C = int(input())
X = int(input())

result = 0
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            if i * 500 + j * 100 + k * 50 == X:
                result += 1
print(result)
