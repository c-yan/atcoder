package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

type segmentTree struct {
	offset int
	data   []int
	op     func(x, y int) int
	e      int
}

func newSegmentTree(n int, op func(x, y int) int, e int) segmentTree {
	var result segmentTree
	t := 1
	for t < n {
		t *= 2
	}
	result.offset = t - 1
	result.data = make([]int, 2*t-1)
	for i := 0; i < len(result.data); i++ {
		result.data[i] = e
	}
	result.op = op
	result.e = e
	return result
}

func (st segmentTree) build(a []int) {
	for i, v := range a {
		st.data[st.offset+i] = v
	}
	for i := st.offset - 1; i > -1; i-- {
		st.data[i] = st.op(st.data[i*2+1], st.data[i*2+2])
	}
}

func (st segmentTree) update(index, value int) {
	i := st.offset + index
	st.data[i] = value
	for i >= 1 {
		i = (i - 1) / 2
		st.data[i] = st.op(st.data[i*2+1], st.data[i*2+2])
	}
}

func (st segmentTree) query(start, stop int) int {
	result := st.e
	l := start + st.offset
	r := stop + st.offset
	for l < r {
		if l&1 == 0 {
			result = st.op(result, st.data[l])
		}
		if r&1 == 0 {
			result = st.op(result, st.data[r-1])
		}
		l = l / 2
		r = (r - 1) / 2
	}
	return result
}

func main() {
	defer flush()

	N := readInt()
	Q := readInt()

	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	st := newSegmentTree(N, max, -1)
	st.build(A)

	for i := 0; i < Q; i++ {
		T := readInt()
		if T == 1 || T == 3 {
			X := readInt()
			V := readInt()
			if T == 1 {
				st.update(X-1, V)
			} else if T == 3 {
				ok := N + 1
				ng := X - 1
				for ok-ng > 1 {
					m := ng + (ok-ng)/2
					if st.query(X-1, m) >= V {
						ok = m
					} else {
						ng = m
					}
				}
				println(ok)
			}
		} else if T == 2 {
			L := readInt()
			R := readInt()
			println(st.query(L-1, R))
		}
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
