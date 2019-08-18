package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	n := readInt()
	q := readInt()

	results := make([]int, n+1)
	parents := make([]int, n+1)

	for i := 0; i < n-1; i++ {
		a := readInt()
		b := readInt()
		parents[b] = a
	}

	for i := 0; i < q; i++ {
		p := readInt()
		x := readInt()
		results[p] += x
	}

	for i := 1; i <= n; i++ {
		results[i] += results[parents[i]]
	}

	for i := 1; i <= n; i++ {
		fmt.Print(results[i])
		if i != n {
			fmt.Print(" ")
		}
	}
	fmt.Println()
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
	result, _ := strconv.Atoi(readString())
	return result
}
