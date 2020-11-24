package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//
const (
	M   = 3001
	INF = M * 1000000000
)

//
var (
	N  int
	a  []int
	dp []int
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func f(l, r, t int) int {
	if l > r {
		return 0
	}
	i := l*M + r
	if dp[i] != INF {
		return dp[i]
	}

	if t == 0 {
		dp[i] = max(f(l+1, r, t^1)+a[l], f(l, r-1, t^1)+a[r])
	} else {
		dp[i] = min(f(l+1, r, t^1)-a[l], f(l, r-1, t^1)-a[r])
	}
	return dp[i]
}

func main() {
	defer flush()

	N = readInt()
	a = make([]int, N)
	for i := 0; i < N; i++ {
		a[i] = readInt()
	}

	dp = make([]int, M*M)
	for i := 0; i < M*M; i++ {
		dp[i] = INF
	}
	println(f(0, N-1, 0))
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
