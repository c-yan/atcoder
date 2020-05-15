package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

//
var (
	N int
	M int
	R int
	r []int
	d [][]int
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func fillInts(a []int, x int) {
	for i := 0; i < len(a); i++ {
		a[i] = x
	}
}

func warshallFloyd(n int, d [][]int) {
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				d[i][j] = min(d[i][j], d[i][k]+d[k][j])
			}
		}
	}
}

func permtationsImpl(a []int, i int, f func(a []int)) {
	if i == len(a)-1 {
		f(a)
		return
	}
	permtationsImpl(a, i+1, f)
	for j := i + 1; j < len(a); j++ {
		a[i], a[j] = a[j], a[i]
		permtationsImpl(a, i+1, f)
		a[i], a[j] = a[j], a[i]
	}
}

func permtations(a []int, f func(a []int)) {
	permtationsImpl(a, 0, f)
}

func main() {
	defer flush()

	N = readInt()
	M = readInt()
	R = readInt()
	r = make([]int, R)
	for i := 0; i < R; i++ {
		r[i] = readInt()
	}

	d = make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		d[i] = make([]int, N+1)
		fillInts(d[i], math.MaxInt32)
		d[i][i] = 0
	}

	for i := 0; i < M; i++ {
		A := readInt()
		B := readInt()
		C := readInt()
		d[A][B] = C
		d[B][A] = C
	}
	warshallFloyd(N+1, d)

	result := math.MaxInt64
	permtations(r, func(a []int) {
		t := 0
		for i := 0; i < R-1; i++ {
			t += d[a[i]][a[i+1]]
		}
		result = min(result, t)
	})
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

func printf(f string, args ...interface{}) (int, error) {
	return fmt.Fprintf(stdoutWriter, f, args...)
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
