package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	N := readInt()
	K := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}
	F := make([]int, N)
	for i := 0; i < N; i++ {
		F[i] = readInt()
	}

	sort.Ints(A)
	sort.Sort(sort.Reverse(sort.IntSlice(F)))

	l := -1            // ng
	r := A[N-1] * F[0] // ok
	for r > l+1 {
		m := l + (r-l)/2
		isOk := func(x int) bool {
			result := 0
			for i := 0; i < N; i++ {
				t := A[i] - x/F[i]
				if t > 0 {
					result += t
				}
			}
			return result <= K
		}
		if isOk(m) {
			r = m
		} else {
			l = m
		}
	}
	fmt.Println(r)
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
