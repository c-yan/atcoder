package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	defer flush()

	N := readInt()
	X := readInt()
	Y := readInt()

	t := make([]int, N)

	for i := 1; i < N; i++ {
		for j := i + 1; j < N+1; j++ {
			t[min(j-i, abs(X-i)+1+abs(Y-j))]++
		}
	}

	for i := 1; i < N; i++ {
		println(t[i])
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
