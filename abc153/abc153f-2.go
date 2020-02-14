// 二分探索, BIT
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

// BIT stands for binary indexed tree.
type BIT []int

func newBIT(n int) BIT {
	return make([]int, n)
}

func (bit BIT) add(i, v int) {
	for i++; i <= len(bit); i += i & -i {
		bit[i-1] += v
	}
}

func (bit BIT) sum(i int) int {
	result := 0
	for i++; i > 0; i -= i & -i {
		result += bit[i-1]
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
	bit := newBIT(N + 1)
	for i := 0; i < N; i++ {
		x, h := XH[i].X, XH[i].H
		h -= bit.sum(i)
		if h <= 0 {
			continue
		}
		result += h
		bit.add(i, h)

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
		bit.add(ng, -h)
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
