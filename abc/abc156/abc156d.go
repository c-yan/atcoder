// フェルマーの小定理
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func mpow(x int, n int) int {
	result := 1
	for n != 0 {
		if n&1 == 1 {
			result *= x
			result %= 1000000007
		}
		x *= x
		x %= 1000000007
		n >>= 1
	}
	return result
}

func mcomb(n int, k int) int {
	a := 1
	b := 1
	for i := 0; i < k; i++ {
		a *= n - i
		a %= 1000000007
		b *= i + 1
		b %= 1000000007
	}
	return a * mpow(b, 1000000005) % 1000000007
}

func main() {
	n := readInt()
	a := readInt()
	b := readInt()

	result := mpow(2, n) - 1
	result -= mcomb(n, a)
	result += 1000000007
	result %= 1000000007
	result -= mcomb(n, b)
	result += 1000000007
	result %= 1000000007
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
