from sys import exit

S = input()
T = input()


def match(s, t):
    for i in range(len(t)):
        if s[i] != '?' and s[i] != t[i]:
            return False
    return True


for i in range(len(S) - len(T), -1, -1):
    if match(S[i: i + len(T)], T):
        print((S[:i] + T + S[i + len(T):]).replace('?', 'a'))
        exit()
print('UNRESTORABLE')
