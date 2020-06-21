// Segment tree
package main

import (
	"bufio"
	"fmt"
	"os"
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
		st.data[st.offset+i] = 1 << uint(v)
	}
	for i := st.offset - 1; i > -1; i-- {
		st.data[i] = st.data[i*2+1] | st.data[i*2+2]
	}
}

func (st segmentTree) update(index, value int) {
	i := st.offset + index
	st.data[i] = 1 << uint(value)
	for i >= 1 {
		i = (i - 1) / 2
		st.data[i] = st.data[i*2+1] | st.data[i*2+2]
	}
}

func (st segmentTree) query(start, stop int) int {
	result := 0
	l := start + st.offset
	r := stop + st.offset
	for l < r {
		if l&1 == 0 {
			result = result | st.data[l]
		}
		if r&1 == 0 {
			result = result | st.data[r-1]
		}
		l = l / 2
		r = (r - 1) / 2
	}
	return result
}

func toInt(s string) int {
	result, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return result
}

func bitCount(a int) int {
	result := 0
	for a != 0 {
		if a&1 == 1 {
			result++
		}
		a >>= 1
	}
	return result
}

func main() {
	defer flush()

	N := readInt()
	S := readString()

	t := make([]int, len(S))
	for i, v := range []byte(S) {
		t[i] = int(v - 'a')
	}

	st := newSegmentTree(N)
	st.updateAll(t)

	Q := readInt()
	for i := 0; i < Q; i++ {
		t := readString()
		if t == "1" {
			i := toInt(readString()) - 1
			c := int([]byte(readString())[0] - 'a')
			st.update(i, c)
		} else if t == "2" {
			l := toInt(readString())
			r := toInt(readString())
			println(bitCount(st.query(l-1, r)))
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

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
