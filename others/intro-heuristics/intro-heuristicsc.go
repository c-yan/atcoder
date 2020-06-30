package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// D
var (
	D int
	c [26]int
	s [][26]int
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	defer flush()

	D = readInt()
	for i := 0; i < 26; i++ {
		c[i] = readInt()
	}
	s = make([][26]int, D)
	for d := 0; d < D; d++ {
		for i := 0; i < 26; i++ {
			s[d][i] = readInt()
		}
	}

	t := make([]int, D)
	for d := 0; d < D; d++ {
		t[d] = readInt() - 1
	}

	M := readInt()
	for m := 0; m < M; m++ {
		d := readInt() - 1
		q := readInt() - 1
		t[d] = q
		last := make([]int, 26)
		S := 0
		for i := 0; i < 26; i++ {
			last[i] = -1
		}
		for d := 0; d < len(t); d++ {
			S += s[d][t[d]]
			last[t[d]] = d
			for i := 0; i < 26; i++ {
				S -= c[i] * (d - last[i])
			}
		}
		println(S)
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
