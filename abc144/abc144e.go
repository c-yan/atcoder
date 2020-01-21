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
	A := readInts(N)
	F := readInts(N)

	sort.Ints(A)
	sort.Sort(sort.Reverse(sort.IntSlice(F)))

	isOk := func(x int) bool {
		trainings := 0
		for i := 0; i < N; i++ {
			t := A[i] - x/F[i]
			if t > 0 {
				trainings += t
			}
		}
		return trainings <= K
	}

	ng := -1
	ok := A[N-1] * F[0]
	for ok-ng > 1 {
		m := ng + (ok-ng)/2
		if isOk(m) {
			ok = m
		} else {
			ng = m
		}
	}
	fmt.Println(ok)
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
