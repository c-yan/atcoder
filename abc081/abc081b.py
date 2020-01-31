N = int(input())
A = list(map(int, input().split()))

result = 0
while True:
    if any(e % 2 == 1 for e in A):
        break
    result += 1
    A = [e // 2 for e in A]
print(result)
