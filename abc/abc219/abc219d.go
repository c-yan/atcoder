package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func conv(x, y int) int {
	return x*301 + y
}

func deconv(n int) (int, int) {
	return n / 301, n % 301
}

func main() {
	defer flush()

	N := readInt()
	X := readInt()
	Y := readInt()

	dp := make([]int, 100000)
	for i := 0; i < 100000; i++ {
		dp[i] = math.MaxInt64
	}
	dp[0] = 0

	m := 0
	for i := 0; i < N; i++ {
		A := readInt()
		B := readInt()
		for j := m; j != -1; j-- {
			if dp[j] == math.MaxInt64 {
				continue
			}
			x, y := deconv(j)
			x += A
			y += B
			if x > 300 {
				x = 300
			}
			if y > 300 {
				y = 300
			}
			k := conv(x, y)
			if dp[k] > dp[j]+1 {
				dp[k] = dp[j] + 1
				m = max(m, k)
			}
		}
	}

	result := math.MaxInt64
	for j := m; j != -1; j-- {
		if dp[j] == math.MaxInt64 {
			continue
		}
		x, y := deconv(j)
		if x < X || y < Y {
			continue
		}
		result = min(result, dp[j])
	}
	if result == math.MaxInt64 {
		println(-1)
	} else {
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
