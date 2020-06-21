package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	m = 1000000007
)

func main() {
	H := readInt()
	W := readInt()
	a := make([]string, 2)
	a[0] = readString()
	a[1] = readString()

	dp := make([][]int, 2)
	dp[0] = make([]int, W)
	dp[1] = make([]int, W)
	dp[0][0] = 1

	for i := 0; i < H-1; i++ {
		for j := 0; j < W-1; j++ {
			if a[0][j+1] != '#' {
				dp[0][j+1] = (dp[0][j+1] + dp[0][j]) % m
			}
			if a[1][j] != '#' {
				dp[1][j] = dp[0][j]
			}
		}
		if a[1][W-1] != '#' {
			dp[1][W-1] = dp[0][W-1]
		}

		a[0], a[1] = a[1], readString()
		dp[0], dp[1] = dp[1], dp[0]
		for j := 0; j < W; j++ {
			dp[1][j] = 0
		}
	}
	for j := 0; j < W-1; j++ {
		if a[0][j+1] != '#' {
			dp[0][j+1] = (dp[0][j+1] + dp[0][j]) % m
		}
	}

	fmt.Println(dp[0][W-1])
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
