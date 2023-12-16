D = list(map(int, input().split()))
J = list(map(int, input().split()))

print(sum(max(D[i], J[i]) for i in range(7)))
