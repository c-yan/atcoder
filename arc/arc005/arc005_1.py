N = int(input())
w = input().split()

result = 0
for e in w:
    if e.rstrip('.') in ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']:
        result += 1
print(result)
