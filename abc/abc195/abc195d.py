N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))

WV.sort(key=lambda x: x[1], reverse=True)
for _ in range(Q):
    L, R = map(lambda x: int(x) - 1, input().split())
    boxes = X[:L] + X[R + 1:]
    boxes.sort()
    result = 0
    for W, V in WV:
        for i in len(boxes):
            if boxes[i] >= W:
                result += V
                boxes = boxes[:i] + boxes[i+1:]
                break
    print(result)
