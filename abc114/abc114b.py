S = input()

print(min(abs(753 - int(S[i:i+3])) for i in range(len(S) - 2)))
