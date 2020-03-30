package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
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
		fmt.Println(t[i])
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
