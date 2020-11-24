package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//
const (
	M = 301
)

//
var (
	dp []float64
	N  int
)

func despread(x, y, z int) int {
	return x*M*M + y*M + z
}

func f(x, y, z int) float64 {
	a := despread(x, y, z)
	if dp[a] != -1.0 {
		return dp[a]
	}
	if a == 0 {
		return 0
	}

	t := float64(N)
	if x != 0 {
		t += f(x-1, y+1, z) * float64(x)
	}
	if y != 0 {
		t += f(x, y-1, z+1) * float64(y)
	}
	if z != 0 {
		t += f(x, y, z-1) * float64(z)
	}
	dp[a] = t / float64(x+y+z)
	return dp[a]
}

func main() {
	defer flush()

	N = readInt()
	a := make([]int, N)
	for i := 0; i < N; i++ {
		a[i] = readInt()
	}

	var t [4]int
	for i := 0; i < N; i++ {
		t[a[i]]++
	}

	dp = make([]float64, M*M*M)
	for i := 0; i < M*M*M; i++ {
		dp[i] = -1.0
	}
	println(f(t[3], t[2], t[1]))
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
