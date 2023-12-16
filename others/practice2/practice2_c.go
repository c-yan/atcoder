package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func floorSum(n, m, a, b int) int {
	result := 0
	if a >= m {
		result += (n - 1) * n * (a / m) / 2
		a %= m
	}
	if b >= m {
		result += n * (b / m)
		b %= m
	}

	yMax := (a*n + b) / m
	xMax := yMax*m - b
	if yMax == 0 {
		return result
	}
	result += (n - (xMax+a-1)/a) * yMax
	result += floorSum(yMax, a, m, (a-xMax%a)%a)
	return result
}

func main() {
	defer flush()

	T := readInt()
	for i := 0; i < T; i++ {
		N := readInt()
		M := readInt()
		A := readInt()
		B := readInt()
		println(floorSum(N, M, A, B))
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

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
