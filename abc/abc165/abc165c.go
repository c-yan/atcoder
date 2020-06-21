package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// N, M, Q
var (
	N          int
	M          int
	Q          int
	a, b, c, d []int
	result     int
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func dfs(A []int) {
	if len(A) == N+1 {
		t := 0
		for i := 0; i < Q; i++ {
			if A[b[i]]-A[a[i]] == c[i] {
				t += d[i]
			}
		}
		result = max(result, t)
		return
	}

	A = append(A, A[len(A)-1])
	for A[len(A)-1] <= M {
		dfs(A)
		A[len(A)-1]++
	}
}

func main() {
	defer flush()

	N = readInt()
	M = readInt()
	Q = readInt()
	a = make([]int, Q)
	b = make([]int, Q)
	c = make([]int, Q)
	d = make([]int, Q)
	for i := 0; i < Q; i++ {
		a[i] = readInt()
		b[i] = readInt()
		c[i] = readInt()
		d[i] = readInt()
	}

	dfs([]int{1})
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

func readInts(n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = readInt()
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

func printIntln(v ...int) {
	b := make([]byte, 0, 4096)
	for i := 0; i < len(v)-1; i++ {
		b = append(b, strconv.Itoa(v[i])...)
		b = append(b, " "...)
	}
	b = append(b, strconv.Itoa(v[len(v)-1])...)
	println(string(b))
}
