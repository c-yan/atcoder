N = int(input())
print(list(sorted(set(map(int, (input() for _ in range(N))))))[-2])
