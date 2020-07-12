package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func popCount(x int) int {
	result := 0
	for x != 0 {
		result += x & 1
		x >>= 1
	}
	return result
}

func f(x int) int {
	if x == 0 {
		return 0
	}
	return 1 + f(x%popCount(x))
}

func main() {
	defer flush()

	N := readInt()
	X := readString()

	c := 0
	for _, b := range []byte(X) {
		if b == '1' {
			c++
		}
	}

	t1, t2 := make([]int, N), make([]int, N)
	t1[0] = 1 % (c + 1)
	if c-1 != 0 {
		t2[0] = 1 % (c - 1)
	}
	for i := 1; i < N; i++ {
		t1[i] = (t1[i-1] << 1) % (c + 1)
		if c-1 != 0 {
			t2[i] = (t2[i-1] << 1) % (c - 1)
		}
	}

	x1, x2 := 0, 0
	for i, b := range []byte(X) {
		if b == '1' {
			x1 += t1[N-1-i]
			if c-1 != 0 {
				x2 += t2[N-1-i]
			}
		}
	}

	for i, b := range []byte(X) {
		if b == '0' {
			n := (x1 + t1[N-1-i]) % (c + 1)
			println(f(n) + 1)
		} else if b == '1' {
			if c-1 == 0 {
				println(0)
				continue
			}
			n := (x2 - t2[N-1-i] + (c - 1)) % (c - 1)
			println(f(n) + 1)
		}
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
