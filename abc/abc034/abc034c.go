// フェルマーの小定理
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	p = 1000000007
)

var (
	fac []int
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func mpow(x int, n int) int {
	result := 1
	for n != 0 {
		if n&1 == 1 {
			result = result * x % p
		}
		x = x * x % p
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
	W := readInt()
	H := readInt()

	n := W + H - 2
	k := min(W-1, H-1)

	fac = make([]int, n+1)
	fac[0] = 1
	for i := 0; i < n; i++ {
		fac[i+1] = fac[i] * (i + 1) % p
	}

	fmt.Println(mcomb(n, k))
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
