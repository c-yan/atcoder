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

func mcomb(n, k int) int {
	a := 1
	b := 1
	for i := 0; i < k; i++ {
		a *= n - i
		a %= m
		b *= i + 1
		b %= m
	}
	return a * mpow(b, m-2) % m
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
