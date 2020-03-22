S = input()


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


N = len(S)

if not is_palindrome(S):
    print('No')
    exit()

if not is_palindrome(S[:(N - 1) // 2]):
    print('No')
    exit()

if not is_palindrome(S[(N + 3) // 2 - 1:]):
    print('No')
    exit()

print('Yes')
