N = int(input())
S = input()

bs = S.encode('us-ascii')
print(bytes((b - 65 + N) % 26 + 65 for b in bs).decode('us-ascii'))
