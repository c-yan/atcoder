package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

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
	cs := make([]int, N+1)
	for i := 0; i < N; i++ {
		x, h := XH[i].X, XH[i].H
		if i != 0 {
			cs[i] += cs[i-1]
		}
		h -= cs[i]
		if h <= 0 {
			continue
		}
		result += h
		cs[i] += h

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
		cs[ng] -= h
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
