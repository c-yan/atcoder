N = int(input())
S = input()

result = S
while True:
    while True:
        t = S.replace('()', '')
        if t == S:
            break
        S = t
    if S == '':
        break
    elif S[0] == ')':
        S = '(' + S
        result = '(' + result
    elif S[0] == '(':
        S = S + ')'
        result = result + ')'
print(result)
