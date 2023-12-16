package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	m = 998244353
)

type tvalue struct {
	n int
	l int
}

var (
	tt []int
	ot []int
)

var (
	defaultValue = tvalue{0, 1}
	defaultLazy  = 0
)

type segmentTree struct {
	offset int
	values []tvalue
	lazy   []int
}

func newSegmentTree(n int) segmentTree {
	var result segmentTree
	t := 1
	for t < n {
		t *= 2
	}
	result.offset = t - 1
	result.values = make([]tvalue, 2*t-1)
	result.lazy = make([]int, 2*t-1)
	for i := 0; i < 2*t-1; i++ {
		result.values[i] = defaultValue
		result.lazy[i] = defaultLazy
	}
	return result
}

func op(x, y tvalue) tvalue {
	return tvalue{(x.n*tt[y.l] + y.n) % m, x.l + y.l}
}

func (st segmentTree) build(a []tvalue) {
	for i, v := range a {
		st.values[st.offset+i] = v
	}
	for i := st.offset - 1; i > -1; i-- {
		st.values[i] = op(st.values[i*2+1], st.values[i*2+2])
	}
}

func (st segmentTree) segments(start, stop int) []int {
	ls := make([]int, 0, 32)
	rs := make([]int, 0, 16)
	l := start + st.offset
	r := stop + st.offset
	for l < r {
		if l&1 == 0 {
			ls = append(ls, l)
		}
		if r&1 == 0 {
			rs = append(rs, r-1)
		}
		l = l / 2
		r = (r - 1) / 2
	}
	for i := 0; i < len(rs)/2; i++ {
		j := len(rs) - 1 - i
		rs[i], rs[j] = rs[j], rs[i]
	}
	return append(ls, rs...)
}

func (st segmentTree) propagate(segments []int) {
	for _, i := range segments {
		indexes := make([]int, 0, 20)
		for i != 0 {
			i = (i - 1) / 2
			indexes = append(indexes, i)
		}
		for j := len(indexes) - 1; j >= 0; j-- {
			k := indexes[j]
			if st.lazy[k] == defaultLazy {
				continue
			}
			l := st.values[k].l / 2
			st.lazy[k*2+1] = st.lazy[k]
			st.values[k*2+1] = tvalue{(ot[l] * st.lazy[k]) % m, l}
			st.lazy[k*2+2] = st.lazy[k]
			st.values[k*2+2] = tvalue{(ot[l] * st.lazy[k]) % m, l}
			st.lazy[k] = defaultLazy
		}
	}
}

func (st segmentTree) apply(start, stop int, value int) {
	segments := st.segments(start, stop)
	st.propagate(segments)
	for _, i := range segments {
		st.lazy[i] = value
		l := st.values[i].l
		st.values[i] = tvalue{(ot[l] * value) % m, l}
		for i != 0 {
			i = (i - 1) / 2
			st.values[i] = op(st.values[i*2+1], st.values[i*2+2])
		}
	}
}

func (st segmentTree) query(start, stop int) tvalue {
	segments := st.segments(start, stop)
	st.propagate(segments)
	result := defaultValue
	for _, i := range segments {
		result = op(result, st.values[i])
	}
	return result
}

func main() {
	defer flush()

	N := readInt()
	Q := readInt()

	tt = make([]int, N+1)
	ot = make([]int, N+1)
	tt[0] = 1
	ot[0] = 0
	for i := 0; i < N; i++ {
		tt[i+1] = (tt[i] * 10) % m
		ot[i+1] = (ot[i] + tt[i]) % m
	}

	st := newSegmentTree(N)
	t := make([]tvalue, N)
	for i := 0; i < N; i++ {
		t[i].n = 1
		t[i].l = 1
	}
	st.build(t)
	for i := 0; i < Q; i++ {
		L := readInt()
		R := readInt()
		D := readInt()
		st.apply(L-1, R, D)
		println(st.query(0, N).n)
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
