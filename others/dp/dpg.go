package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func f(i int, links [][]int, dp []int) int {
	if dp[i] != -1 {
		return dp[i]
	}
	if len(links[i]) == 0 {
		dp[i] = 0
	} else {
		t := -1
		for _, j := range links[i] {
			t = max(t, f(j, links, dp))
		}
		dp[i] = t + 1
	}
	return dp[i]
}

func main() {
	defer flush()

	N := readInt()
	M := readInt()

	links := make([][]int, N)
	for i := 0; i < M; i++ {
		x := readInt() - 1
		y := readInt() - 1
		links[x] = append(links[x], y)
	}

	dp := make([]int, N)
	for i := 0; i < N; i++ {
		dp[i] = -1
	}

	result := -1
	for i := 0; i < N; i++ {
		result = max(result, f(i, links, dp))
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
