N = int(input())

print(sorted(set(map(int, (input() for _ in range(N)))))[-2])
