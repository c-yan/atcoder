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

func mpow(x int, n int) int {
	result := 1
	for n != 0 {
		if n&1 == 1 {
			result *= x
			result %= m
		}
		x *= x
		x %= m
		n >>= 1
	}
	return result
}

func mcomb(n int, k int) int {
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

func main() {
	n := readInt()
	a := readInt()
	b := readInt()

	result := mpow(2, n) - 1
	result -= mcomb(n, a)
	result += m
	result %= m
	result -= mcomb(n, b)
	result += m
	result %= m
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
