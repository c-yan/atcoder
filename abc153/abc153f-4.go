// 二分探索, SegmentTree
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

type t struct {
	X int
	H int
}
type byX []t

func (a byX) Len() int           { return len(a) }
func (a byX) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a byX) Less(i, j int) bool { return a[i].X < a[j].X }

func main() {
	N := readInt()
	D := readInt()
	A := readInt()
	XH := make([]t, N)
	for i := 0; i < N; i++ {
		XH[i].X = readInt()
		XH[i].H = (readInt() + A - 1) / A
	}

	sort.Sort(byX(XH))
	result := 0
	st := newSegmentTree(N + 1)
	for i := 0; i < N; i++ {
		x, h := XH[i].X, XH[i].H
		h -= st.query(0, i+1)
		if h <= 0 {
			continue
		}
		result += h
		st.add(i, h)

		ok := i
		ng := N
		for ng-ok != 1 {
			m := ok + (ng-ok)/2
			if XH[m].X <= x+2*D {
				ok = m
			} else {
				ng = m
			}
		}
		st.add(ng, -h)
	}
	fmt.Println(result)
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
