H, W = map(int, input().split())
R, C = map(int, input().split())

result = 0
if R != 1:
    result += 1
if C != 1:
    result += 1
if R != H:
    result += 1
if C != W:
    result += 1
print(result)
