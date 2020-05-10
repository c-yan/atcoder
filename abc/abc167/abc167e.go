// フェルマーの小定理
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	p = 998244353
)

var (
	fac []int
)

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
	defer flush()

	N := readInt()
	M := readInt()
	K := readInt()

	fac = make([]int, N+1)
	fac[0] = 1
	for i := 0; i < N; i++ {
		fac[i+1] = fac[i] * (i + 1) % p
	}

	result := 0
	for i := 0; i < K+1; i++ {
		t := M * mcomb(N-1, i)
		t %= p
		t *= mpow(M-1, N-1-i)
		t %= p
		result += t
		result %= p
	}
	println(result)
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

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func printf(f string, args ...interface{}) (int, error) {
	return fmt.Fprintf(stdoutWriter, f, args...)
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
