package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	defer flush()

	N := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	r := make([]int, N)
	for i := N - 1; i >= 0; i-- {
		j := i + 1
		for j < N {
			if A[j] < A[i] {
				break
			}
			j = r[j]
		}
		r[i] = j
	}

	result := 0
	l := make([]int, N)
	for i := 0; i < N; i++ {
		j := i
		for j > 0 {
			if A[j-1] < A[i] {
				break
			}
			j = l[j-1]
		}
		l[i] = j
		result = max(result, A[i]*(r[i]-l[i]))
	}
	println(result)
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

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
