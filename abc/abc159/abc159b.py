S = input()


def is_palindrome(s):
    return s == s[::-1]


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
