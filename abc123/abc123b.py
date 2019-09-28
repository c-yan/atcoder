A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
a = [A, B, C, D, E]
a.sort(key=lambda x: (x+9) % 10, reverse=True)
print(sum((i + 9) // 10 * 10 for i in a[:4]) + a[4])
