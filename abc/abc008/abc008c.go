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
	C := make([]int, N)
	for i := 0; i < N; i++ {
		C[i] = readInt()
	}

	result := 0.0
	for i := 0; i < N; i++ {
		c := -1
		for j := 0; j < N; j++ {
			if C[i]%C[j] == 0 {
				c++
			}
		}
		result += float64(c/2+1) / float64(c+1)
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

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
