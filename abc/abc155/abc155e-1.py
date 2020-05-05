N = input()

N = '0' + N
result = 0
carry = 0
for i in range(len(N) - 1, 0, -1):
    c = int(N[i]) + carry
    n = int(N[i - 1])
    if c < 5 or (c == 5 and n < 5):
        result += c
        carry = 0
    else:
        result += 10 - c
        carry = 1
result += carry
print(result)
