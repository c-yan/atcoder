a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

coordinates = [a, b, c, d, e]
for i in range(5):
    for j in range(i + 1, 5):
        if coordinates[j] - coordinates[i] > k:
            print(':(')
            exit()
print('Yay!')
