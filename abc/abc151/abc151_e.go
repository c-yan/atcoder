// フェルマーの小定理
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const (
	m = 1000000007
)

func mpow(x, y int) int {
	result := 1
	for y != 0 {
		if y&1 == 1 {
			result *= x
			result %= m
		}
		x *= x
		x %= m
		y >>= 1
	}
	return result
}

var (
	fac []int
)

func initFactorialTable(n int) {
	fac = make([]int, n+1)
	fac[0] = 1
	for i := 0; i < n; i++ {
		fac[i+1] = fac[i] * (i + 1) % m
	}
}

func mcomb(n, k int) int {
	if n == 0 && k == 0 {
		return 1
	}
	if n < k || k < 0 {
		return 0
	}
	return (fac[n] * mpow(fac[n-k], m-2) % m) * mpow(fac[k], m-2) % m
}

func main() {
	N := readInt()
	K := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	initFactorialTable(N - 1)

	sort.Sort(sort.Reverse(sort.IntSlice(A)))
	maxX := 0
	for i := 0; i < N-K+1; i++ {
		maxX += A[i] * mcomb(N-(i+1), K-1)
		maxX %= m
	}

	sort.Ints(A)
	minX := 0
	for i := 0; i < N-K+1; i++ {
		minX += A[i] * mcomb(N-(i+1), K-1)
		minX %= m
	}

	// maxX も minX も負の可能性があるので正に揃える
	maxX += m
	maxX %= m
	minX += m
	minX %= m

	fmt.Println((maxX - minX + m) % m)
}

const (
	ioBufferSize = 1 * 1024 * 1024 // 1 MB
)

var stdinScanner = func() *bufio.Scanner {
	result := bufio.NewScanner(os.Stdin)
	result.Buffer(make([]byte, ioBufferSize), ioBufferSize)
	result.Split(bufio.ScanWords)
	return result
}()

func readString() string {
	stdinScanner.Scan()
	return stdinScanner.Text()
}

func readInt() int {
	result, err := strconv.Atoi(readString())
	if err != nil {
		panic(err)
	}
	return result
}
