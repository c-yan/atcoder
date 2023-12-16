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
	damage := 0
	q := make([]t, 0)
	for i := 0; i < N; i++ {
		x, h := XH[i].X, XH[i].H
		for len(q) != 0 {
			if x <= q[0].X {
				break
			}
			damage -= q[0].H
			q = q[1:]
		}
		h -= damage
		if h <= 0 {
			continue
		}
		result += h
		damage += h
		q = append(q, t{x + 2*D, h})
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
