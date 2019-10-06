A, B, C = map(int, input().split())

# 1. 3つとも違う数字
#  => 小さいふたつを + 1
# 2. 2つ同じ数字
#  => 1つだけの数字が小さい
#     小さい数字を + 2
#  => 1つだけの数字が大きい
#     小さいふたつを + 1
result = 0
while True:
    if A == B and B == C:
        break
    elif A != B and B != C and A != C:
        if A < B:
            if B < C:
                A += 1
                B += 1
            else:
                A += 1
                C += 1
        else:
            if A < C:
                A += 1
                B += 1
            else:
                B += 1
                C += 1
    else:
        if A == B:
            if A > C:
                C += 2
            else:
                A += 1
                B += 1
        elif B == C:
            if A > B:
                B += 1
                C += 1
            else:
                A += 2
        else:
            # A == C
            if A > B:
                B += 2
            else:
                A += 1
                C += 1
    result += 1
print(result)
