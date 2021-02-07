n, k = map(int, input().split())
s = input()

def get_winner(a, b):
    if a == b:
        return a
    if a > b:
        a, b = b, a
    if a == 'P':
        if b == 'R':
            return 'P'
        elif b == 'S':
            return 'S'
    elif a == 'R':
        return 'R'

while k != 0:
    if len(s) % 2 == 1:
        s = s + s
    elif len(s) % 2 == 0:
        k -= 1
        t = ''
        for i in range(0, len(s), 2):
            t += get_winner(s[i], s[i + 1])
        s = t
print(s[0])
