N = int(input())
S = input()

print(''.join(chr((ord(c) - ord('A') + N) % 26 + ord('A')) for c in S))
