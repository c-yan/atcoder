N = int(input())
s = [input() for _ in range(5)]

a = [
    '.###..#..###.###.#.#.###.###.###.###.###.',
    '.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.',
    '.#.#..#..###.###.###.###.###...#.###.###.',
    '.#.#..#..#.....#...#...#.#.#...#.#.#...#.',
    '.###.###.###.###...#.###.###...#.###.###.'
]

result = []
for i in range(N):
    t = [s[j][i * 4:(i + 1) * 4] for j in range(5)]
    for j in range(10):
        for k in range(5):
            if t[k] != a[k][j * 4:(j + 1) * 4]:
                break
        else:
            result.append(j)
            break
print(''.join(str(i) for i in result))
