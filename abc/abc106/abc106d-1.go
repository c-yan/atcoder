// 累積和
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	defer flush()

	N := readInt()
	M := readInt()
	Q := readInt()

	t := make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		t[i] = make([]int, N+1)
	}

	for i := 0; i < M; i++ {
		L := readInt()
		R := readInt()
		t[L][R]++
	}

	for i := 0; i < N+1; i++ {
		for j := 0; j < N; j++ {
			t[i][j+1] += t[i][j]
		}
	}

	for i := 0; i < Q; i++ {
		p := readInt()
		q := readInt()
		result := 0
		for i := p; i < q+1; i++ {
			result += t[i][q] - t[i][i-1]
		}
		println(result)
	}
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
