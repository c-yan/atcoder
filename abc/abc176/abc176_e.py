H, W, M = map(int, input().split())

rows = [0] * H
cols = [0] * W
s = set()
for _ in range(M):
    h, w = map(lambda x: int(x) - 1,input().split())
    rows[h] += 1
    cols[w] += 1
    s.add((h, w))

max_rows = max(rows)
max_cols = max(cols)

max_rows_indexes = [i for i in range(H) if rows[i] == max_rows]
max_cols_indexes = [i for i in range(W) if cols[i] == max_cols]

duplicate = True
if M >= len(max_rows_indexes) * len(max_cols_indexes):
    for h in max_rows_indexes:
        for w in max_cols_indexes:
            if (h, w) not in s:
                duplicate = False
                break
        if not duplicate:
            break
else:
    duplicate = False

if duplicate:
    print(max_rows + max_cols - 1)
else:
    print(max_rows + max_cols)
