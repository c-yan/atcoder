A = int(input())
B = int(input())

print(*(set([1, 2, 3]) - set([A, B])))
