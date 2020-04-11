package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	defer flush()

	N := readInt()
	K := readInt()

	c := make([][]int, 2000+1)
	for i := 0; i < 2000+1; i++ {
		c[i] = make([]int, 2000+1)
	}
	c[0][0] = 1
	for i := 0; i < 2000+1; i++ {
		c[i][0] = 1
		for j := 1; j < i+1; j++ {
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % 1000000007
		}
	}

	f := func(n, k int) int {
		return c[n+k-1][k-1]
	}

	for i := 1; i <= K; i++ {
		println(f(K-i, i) * f(N-K-(i-1), i+1) % 1000000007)
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
