package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func isqrt(n int) int {
	if n < 0 {
		panic("isqrt argument must be nonnegative")
	}

	if n <= 1 {
		return n
	}

	ok := 0
	ng := 3037000500 // 3037000499 * 3037000499 < math.MaxInt64 < 3037000500 * 3037000500
	if n < ng {
		ng = n
	}
	for ng-ok > 1 {
		m := ok + (ng-ok)/2
		if m*m <= n {
			ok = m
		} else {
			ng = m
		}
	}
	return ok
}

func gcd(x, y int) int {
	if x < y {
		x, y = y, x
	}
	for y > 0 {
		x, y = y, x%y
	}
	return x
}

func main() {
	defer flush()

	A := readInt()
	B := readInt()

	N := gcd(A, B)
	if N == 1 {
		println(1)
		return
	}

	result := 1
	for x := 2; x < isqrt(N)+1; x++ {
		if N%x == 0 {
			result++
			for N%x == 0 {
				N /= x
			}
			if N == 1 {
				break
			}
		}
	}
	if N != 1 {
		result++
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
