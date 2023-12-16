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
	W := readInt()
	H := readInt()

	n := (W - 1) + (H - 1)
	k := min(W-1, H-1)

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
