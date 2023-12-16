package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func f(cy, cx, K int, t [][]int) bool {
	for y := cy - (K - 1); y < cy+K; y++ {
		l := cx - (K - 1) + abs(y-cy)
		r := cx + (K - 1) - abs(y-cy)
		if l == 0 {
			if t[y][r] != 0 {
				return false
			}
		} else {
			if t[y][r]-t[y][l-1] != 0 {
				return false
			}
		}
	}
	return true
}

func main() {
	defer flush()

	R := readInt()
	C := readInt()
	K := readInt()

	s := make([]string, R)
	for i := 0; i < R; i++ {
		s[i] = readString()
	}

	t := make([][]int, R)
	for i := 0; i < R; i++ {
		t[i] = make([]int, C)
	}

	for y := 0; y < R; y++ {
		for x := 0; x < C; x++ {
			if s[y][x] == 'x' {
				t[y][x] = 1
			}
			if x != 0 {
				t[y][x] += t[y][x-1]
			}
		}
	}

	result := 0
	for y := K - 1; y < R-(K-1); y++ {
		for x := K - 1; x < C-(K-1); x++ {
			if f(y, x, K, t) {
				result++
			}
		}
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
