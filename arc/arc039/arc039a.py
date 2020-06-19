A, B = input().split()

t = list(A)
if t[0] != '9':
    t[0] = '9'
elif t[1] != '9':
    t[1] = '9'
elif t[2] != '9':
    t[2] = '9'

a = int(''.join(t))
result = a - int(B)

t = list(B)
if t[0] != '1':
    t[0] = '1'
elif t[1] != '0':
    t[1] = '0'
elif t[2] != '0':
    t[2] = '0'

b = int(''.join(t))
result = max(result, int(A) - b)
print(result)
