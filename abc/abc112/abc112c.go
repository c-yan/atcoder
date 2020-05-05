package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type cxcyh struct {
	CX int
	CY int
	H  int
}

type xyh struct {
	x int
	y int
	h int
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	N := readInt()
	XYH := make([]xyh, 0, N)
	n := -1
	for i := 0; i < N; i++ {
		x := readInt()
		y := readInt()
		h := readInt()
		XYH = append(XYH, xyh{x, y, h})
		if h != 0 {
			n = i
		}
	}

	q := make([]cxcyh, 0, 101*101)
	for cx := 0; cx <= 100; cx++ {
		for cy := 0; cy <= 100; cy++ {
			H := XYH[n].h + abs(XYH[n].x-cx) + abs(XYH[n].y-cy)
			q = append(q, cxcyh{cx, cy, H})
		}
	}

	for i := 0; i < len(XYH); i++ {
		nq := make([]cxcyh, 0, len(q))
		for j := 0; j < len(q); j++ {
			if XYH[i].h == max(q[j].H-abs(XYH[i].x-q[j].CX)-abs(XYH[i].y-q[j].CY), 0) {
				nq = append(nq, q[j])
			}
		}
		q = nq
	}

	fmt.Printf("%d %d %d\n", q[0].CX, q[0].CY, q[0].H)
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
