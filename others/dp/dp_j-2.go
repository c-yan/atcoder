package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//
const (
	M = 301
)

func despread(x, y, z int) int {
	return x*M*M + y*M + z
}

func main() {
	defer flush()

	N := readInt()
	a := make([]int, N)
	for i := 0; i < N; i++ {
		a[i] = readInt()
	}

	var c [4]int
	for i := 0; i < N; i++ {
		c[a[i]]++
	}

	dp := make([]float64, M*M*M)
	for x := 0; x <= c[3]; x++ {
		for y := 0; y <= c[3]+c[2]; y++ {
			for z := 0; z <= c[3]+c[2]+c[1]; z++ {
				a := despread(x, y, z)
				if a == 0 {
					continue
				}

				t := float64(N)
				if x != 0 {
					t += dp[despread(x-1, y+1, z)] * float64(x)
				}
				if y != 0 {
					t += dp[despread(x, y-1, z+1)] * float64(y)
				}
				if z != 0 {
					t += dp[despread(x, y, z-1)] * float64(z)
				}
				dp[a] = t / float64(x+y+z)
			}
		}
	}
	println(dp[despread(c[3], c[2], c[1])])
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
