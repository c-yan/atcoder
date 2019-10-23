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
	L := make([]int, N)
	for i := 0; i < N; i++ {
		L[i] = readInt()
	}

	sort.Ints(L)
	result := 0
	for i := 0; i < N-2; i++ {
		for j := i + 1; j < N-1; j++ {
			x := L[i] + L[j]
			for k := j + 1; k < N; k++ {
				if L[k] >= x {
					break
				}
				result++
			}
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
