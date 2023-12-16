package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//
const (
	M = 101
)

//
var (
	A  int
	B  int
	C  int
	dp []float64
)

func despread(x, y, z int) int {
	return x*M*M + y*M + z
}

func main() {
	defer flush()

	A = readInt()
	B = readInt()
	C = readInt()

	dp = make([]float64, despread(100, 100, 100)+1)
	dp[despread(A, B, C)] = 1.0

	for i := A; i < 100; i++ {
		for j := B; j < 100; j++ {
			for k := C; k < 100; k++ {
				if i+j+k == A+B+C {
					continue
				}

				t := 0.0
				if i != 0 {
					t += dp[despread(i-1, j, k)] * float64(i-1)
				}
				if j != 0 {
					t += dp[despread(i, j-1, k)] * float64(j-1)
				}
				if k != 0 {
					t += dp[despread(i, j, k-1)] * float64(k-1)
				}
				dp[despread(i, j, k)] = t / float64(i+j+k-1)
			}
		}
	}

	result := 0.0
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			t := 0.0
			t += dp[despread(99, i, j)]
			t += dp[despread(i, 99, j)]
			t += dp[despread(i, j, 99)]
			result += float64((100+i+j)-(A+B+C)) * t * 99 / float64(99+i+j)
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
