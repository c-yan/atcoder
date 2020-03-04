package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const (
	p = 1000000007
)

var (
	fac []int
)

func mpow(x int, n int) int {
	result := 1
	for n != 0 {
		if n&1 == 1 {
			result *= x
			result %= p
		}
		x *= x
		x %= p
		n >>= 1
	}
	return result
}

func mcomb(n int, k int) int {
	if n == 0 && k == 0 {
		return 1
	}
	if n < k || k < 0 {
		return 0
	}
	return (fac[n] * mpow(fac[n-k], p-2) % p) * mpow(fac[k], p-2) % p
}

func main() {
	N := readInt()
	K := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	fac = make([]int, N+1)
	fac[0] = 1
	for i := 0; i < N; i++ {
		fac[i+1] = fac[i] * (i + 1) % p
	}

	sort.Sort(sort.Reverse(sort.IntSlice(A)))
	result := 0
	for i := 0; i < N-K+1; i++ {
		result += A[i] * mcomb(N-(i+1), K-1)
		result %= p
	}

	sort.Ints(A)
	t := 0
	for i := 0; i < N-K+1; i++ {
		t += A[i] * mcomb(N-(i+1), K-1)
		t %= p
	}

	result -= t
	result %= p
	result += p
	result %= p
	fmt.Println(result)
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
