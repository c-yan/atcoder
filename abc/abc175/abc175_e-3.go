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

func main() {
	defer flush()

	R := readInt()
	C := readInt()
	K := readInt()

	goods := make([][]int, R)
	for i := 0; i < R; i++ {
		goods[i] = make([]int, C)
	}
	for i := 0; i < K; i++ {
		r := readInt() - 1
		c := readInt() - 1
		v := readInt()
		goods[r][c] = v
	}

	dp := make([]int, C+1)
	cur := make([]int, 4)
	for i := 0; i < R; i++ {
		for k := 0; k < 4; k++ {
			cur[k] = 0
		}
		cur[0] = dp[0]
		for j := 0; j < C; j++ {
			if goods[i][j] != 0 {
				for k := 2; k >= 0; k-- {
					cur[k+1] = max(cur[k+1], cur[k]+goods[i][j])
				}
			}
			for k := 0; k < 4; k++ {
				dp[j] = max(dp[j], cur[k])
			}
			cur[0] = max(cur[0], dp[j+1])
		}
	}

	result := -1
	for k := 0; k < 4; k++ {
		result = max(result, cur[k])
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
