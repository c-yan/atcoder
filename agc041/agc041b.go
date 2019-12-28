package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	N := readInt()
	M := readInt()
	V := readInt()
	P := readInt()

	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}
	sort.Sort(sort.Reverse(sort.IntSlice(A)))
	p := A[P-1]
	V -= P - 1
	b := A[P-1:]
	for {
		mv := M * V
		for i := 0; i < len(b); i++ {
			t := min(p-b[i], M)
			mv -= t
		}
		if mv > 0 {
			p += (mv + len(b) - 1) / len(b)
		} else {
			break
		}
	}

	result := 0
	for i := 0; i < N; i++ {
		if A[i]+M >= p {
			result++
		}
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
