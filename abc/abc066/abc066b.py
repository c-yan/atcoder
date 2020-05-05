S = input()

t = (len(S) - 1) // 2 * 2
while True:
    if S[:t//2] == S[t//2:t]:
        break
    t -= 2
print(t)
