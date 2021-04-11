N = input()

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

for i in range(len(N) + 1):
    if is_palindrome('0' * i + N):
        print('Yes')
        break
else:
    print('No')
