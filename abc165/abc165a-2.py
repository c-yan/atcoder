K = int(input())
A, B = map(int, input().split())

if (B // K) * K >= A:
    print('OK')
else:
    print('NG')
