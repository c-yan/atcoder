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

func main() {
	defer flush()

	N := readInt()

	if N == 2 {
		// K = 2
		println(1)
		return
	}

	result := 2 // K = N - 1, N
	for K := 2; K <= isqrt(N); K++ {
		t := N
		for t >= K && t%K == 0 {
			t /= K
		}
		if t%K == 1 {
			result++
		}

		if (N-1)%K == 0 && (N-1)/K > K {
			result++
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
