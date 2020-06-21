// フェルマーの小定理
package main

import (
	"bufio"
	"fmt"
	"os"
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

func mcomb(n, k int) int {
	if n == 0 && k == 0 {
		return 1
	}
	if n < k || k < 0 {
		return 0
	}
	return (fac[n] * mpow(fac[n-k], m-2) % m) * mpow(fac[k], m-2) % m
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	X := readInt()
	Y := readInt()

	if (X+Y)%3 != 0 {
		fmt.Println(0)
		return
	}

	a := (2*Y - X) / 3
	b := (2*X - Y) / 3

	if a < 0 || b < 0 {
		fmt.Println(0)
		return
	}

	n := a + b
	k := min(a, b)

	fac = make([]int, n+1)
	fac[0] = 1
	for i := 0; i < n; i++ {
		fac[i+1] = fac[i] * (i + 1) % m
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
