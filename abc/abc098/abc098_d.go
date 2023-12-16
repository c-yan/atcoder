// しゃくとり法
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	N := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	result := 0
	r := 0
	xs := A[0]
	cs := A[0]
	for l := 0; l < N; l++ {
		for r < N-1 && xs^A[r+1] == cs+A[r+1] {
			r++
			xs ^= A[r]
			cs += A[r]
		}
		result += r - l + 1
		xs ^= A[l]
		cs -= A[l]
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
