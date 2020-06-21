package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

type sparseTable struct {
	data   [][]int
	lookup []int
	f      func(a, b int) int
}

func newSparseTable(a []int) sparseTable {
	f := min
	b := 0
	for (1 << b) <= len(a) {
		b++
	}
	data := make([][]int, b)
	for i := 0; i < b; i++ {
		data[i] = make([]int, 1<<b)
	}
	copy(data[0][:len(a)], a)
	for i := 1; i < b; i++ {
		for j := 0; j+(1<<i) <= (1 << b); j++ {
			data[i][j] = f(data[i-1][j], data[i-1][j+(1<<(i-1))])
		}
	}
	lookup := make([]int, len(a)+1)
	for i := 2; i < len(lookup); i++ {
		lookup[i] = lookup[i>>1] + 1
	}

	var result sparseTable
	result.f = f
	result.data = data
	result.lookup = lookup
	return result
}

func (st sparseTable) query(start, stop int) int {
	b := st.lookup[stop-start]
	return st.f(st.data[b][start], st.data[b][stop-(1<<b)])
}

func main() {
	defer flush()

	N := readInt()
	K := readInt()
	D := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	if 1+(K-1)*D > N {
		println(-1)
		return
	}

	st := newSparseTable(A)

	result := make([]int, 0, K)
	i := 0
	for k := K - 1; k >= 0; k-- {
		m := st.query(i, N-k*D)
		result = append(result, m)
		for A[i] != m {
			i++
		}
		i += D
	}

	for i := 0; i < len(result); i++ {
		println(result[i])
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
