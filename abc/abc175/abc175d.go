package main

import (
	"bufio"
	"fmt"
	"math"
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
	K := readInt()

	P := make([]int, N)
	for i := 0; i < N; i++ {
		P[i] = readInt()
	}
	C := make([]int, N)
	for i := 0; i < N; i++ {
		C[i] = readInt()
	}

	result := math.MinInt64
	for i := 0; i < N; i++ {
		p := P[i] - 1
		c := C[p]
		k := K - 1
		t := c
		for p != i && k != 0 {
			p = P[p] - 1
			c += C[p]
			t = max(t, c)
			k--
		}
		if k == 0 || c <= 0 {
			result = max(result, t)
			continue
		}
		l := K - k
		c = c * (K/l - 1)
		k = K - (K/l-1)*l
		t = c
		for k != 0 {
			p = P[p] - 1
			c += C[p]
			t = max(t, c)
			k--
		}
		result = max(result, t)
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
