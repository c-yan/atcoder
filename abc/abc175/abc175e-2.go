package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

var (
	dp    [3001][3001][4]int
	goods [3000][3000]int
)

func main() {
	defer flush()

	R := readInt()
	C := readInt()
	K := readInt()
	for i := 0; i < K; i++ {
		r := readInt() - 1
		c := readInt() - 1
		v := readInt()
		goods[r][c] = v
	}

	for i := 0; i < R; i++ {
		for j := 0; j < C; j++ {
			if goods[i][j] != 0 {
				for k := 2; k >= 0; k-- {
					dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k]+goods[i][j])
				}
			}
			for k := 0; k < 4; k++ {
				dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k])
				dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][k])
			}
		}
	}

	result := -1
	for k := 0; k < 4; k++ {
		result = max(result, dp[R-1][C-1][k])
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
