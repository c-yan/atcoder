// パスカルの三角形
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

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	defer flush()

	N := readInt()
	K := readInt()

	n := max(K, N-K+1)
	c := make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		c[i] = make([]int, n+1)
	}
	c[0][0] = 1
	for i := 0; i < n+1; i++ {
		c[i][0] = 1
		for j := 1; j < i+1; j++ {
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % m
		}
	}

	for i := 1; i <= K; i++ {
		println(c[K-1][i-1] * c[N-K+1][i] % m)
	}
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
