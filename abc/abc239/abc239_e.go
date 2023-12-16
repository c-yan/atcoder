package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var (
	X     []int
	links [][]int
	lut   [21]map[int]int
)

func f(k int, i int, p int) []int {
	t := make([]int, 0, 20)
	t = append(t, X[i])
	for _, x := range links[i] {
		if x == p {
			continue
		}
		t = append(t, f(k, x, i)...)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(t)))
	if len(t) >= k {
		lut[k][i] = t[k-1]
	}
	return t[:k]
}

func main() {
	defer flush()

	N := readInt()
	Q := readInt()
	X = make([]int, N)
	for i := 0; i < N; i++ {
		X[i] = readInt()
	}

	links = make([][]int, N)

	for i := 0; i < N-1; i++ {
		A := readInt() - 1
		B := readInt() - 1
		links[A] = append(links[A], B)
		links[B] = append(links[B], A)
	}

	for i := 0; i < Q; i++ {
		V := readInt() - 1
		K := readInt()
		if lut[K] == nil {
			lut[K] = make(map[int]int)
			f(K, 0, -1)
		}
		println(lut[K][V])
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
