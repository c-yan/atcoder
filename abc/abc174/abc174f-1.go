// Segment tree (Sum)
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type segmentTree struct {
	data   []int
	offset int
}

func newSegmentTree(n int) segmentTree {
	var result segmentTree
	t := 1
	for t < n {
		t *= 2
	}
	result.offset = t - 1
	result.data = make([]int, 2*t-1)
	return result
}

func (st segmentTree) updateAll(a []int) {
	for i, v := range a {
		st.data[st.offset+i] = v
	}
	for i := st.offset - 1; i > -1; i-- {
		st.data[i] = st.data[i*2+1] + st.data[i*2+2]
	}
}

func (st segmentTree) add(index, value int) {
	i := st.offset + index
	st.data[i] += value
	for i >= 1 {
		i = (i - 1) / 2
		st.data[i] = st.data[i*2+1] + st.data[i*2+2]
	}
}

func (st segmentTree) update(index, value int) {
	i := st.offset + index
	st.data[i] = value
	for i >= 1 {
		i = (i - 1) / 2
		st.data[i] = st.data[i*2+1] + st.data[i*2+2]
	}
}

func (st segmentTree) query(start, stop int) int {
	result := 0
	l := start + st.offset
	r := stop + st.offset
	for l < r {
		if l&1 == 0 {
			result += st.data[l]
		}
		if r&1 == 0 {
			result += st.data[r-1]
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

	c := make([]int, N)
	for i := 0; i < N; i++ {
		c[i] = readInt()
	}

	lr := make([][3]int, Q)
	for i := 0; i < Q; i++ {
		l := readInt() - 1
		r := readInt() - 1
		lr[i] = [3]int{i, l, r}
	}
	sort.Slice(lr, func(i, j int) bool { return lr[i][2] < lr[j][2] })

	result := make([]int, Q)
	st := newSegmentTree(N)
	mr := map[int]int{}
	k := 0
	for i := 0; i < N; i++ {
		if j, ok := mr[c[i]]; ok {
			st.add(j, -1)
		}
		st.add(i, 1)
		mr[c[i]] = i
		for k < Q && lr[k][2] == i {
			result[lr[k][0]] = st.query(lr[k][1], lr[k][2]+1)
			k++
		}
	}

	for i := 0; i < Q; i++ {
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
