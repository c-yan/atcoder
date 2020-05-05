X = int(input())

result = (X // 500) * 1000
X -= (X // 500) * 500
result += (X // 5) * 5
print(result)
