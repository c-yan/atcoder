package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	X := readInt()
	Y := readInt()
	A := readInt()
	B := readInt()
	C := readInt()

	p := make([]int, A+1)
	q := make([]int, B+1)
	r := make([]int, C+1)

	for i := 0; i < A; i++ {
		p[i+1] = readInt()
	}
	for i := 0; i < B; i++ {
		q[i+1] = readInt()
	}
	for i := 0; i < C; i++ {
		r[i+1] = readInt()
	}

	sort.Sort(sort.Reverse(sort.IntSlice(p[1:])))
	sort.Sort(sort.Reverse(sort.IntSlice(q[1:])))
	sort.Sort(sort.Reverse(sort.IntSlice(r[1:])))

	p = p[:X+1]
	q = q[:Y+1]

	for i := 1; i < X; i++ {
		p[i+1] += p[i]
	}
	for i := 1; i < Y; i++ {
		q[i+1] += q[i]
	}
	for i := 1; i < C; i++ {
		r[i+1] += r[i]
	}

	result := 0
	for i := max(0, X-C); i <= X; i++ {
		ok := max(0, Y-(C-(X-i))) - 1
		ng := Y
		for ng-ok != 1 {
			m := ok + (ng-ok)/2
			t0 := q[m] + r[(X-i)+(Y-m)]
			t1 := q[m+1] + r[(X-i)+(Y-(m+1))]
			if t0 < t1 {
				ok = m
			} else {
				ng = m
			}
		}
		j := ok + 1
		result = max(result, p[i]+q[j]+r[(X-i)+(Y-j)])
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
