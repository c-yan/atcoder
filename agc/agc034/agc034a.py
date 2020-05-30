N, A, B, C, D = map(int, input().split())
S = input()


def move_snuke():
    global A, B
    if B == D:
        return False
    if S[B + 1] == '.' and A != B + 1:
        B += 1
        return True
    if S[B + 2] == '.' and A != B + 2:
        B += 2
        return True
    return False


def move_fnuke():
    global A, B
    if A == C:
        return False
    if S[A + 1] == '.' and B != A + 1:
        A += 1
        return True
    if S[A + 2] == '.' and B != A + 2:
        A += 2
        return True
    return False


S = '#' + S
while True:
    if C < D:
        if not move_snuke():
            if not move_fnuke():
                print('No')
                break
    else:
        if not move_fnuke():
            if not move_snuke():
                print('No')
                break
    if A == C and B == D:
        print('Yes')
        break
