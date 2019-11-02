# パスカルの三角形
def main():
    N, K = map(int, input().split())

    c = [[0] * 4000 for _ in range(4000)]
    c[0][0] = 1
    for i in range(1, 4000):
        ci = c[i]
        ci1 = c[i - 1]
        ci[0] = 1
        for j in range(1, i + 1):
            ci[j] = (ci1[j - 1] + ci1[j]) % 1000000007

    def f(n, k):
        return c[n+k-1][k-1]

    for i in range(1, K + 1):
        print((f(K-i, i) * f(N-K-(i-1), i+1)) % 1000000007)


main()
