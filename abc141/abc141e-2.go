// DP(貰うDP)
package main

import (
	"bufio"
	"fmt"
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

func main() {
	N := readInt()
	S := readString()

	dp := make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		dp[i] = make([]int, N+1)
	}

	result := 0
	for i := N - 1; i > -1; i-- {
		for j := N - 1; j > -1; j-- {
			if S[i] == S[j] {
				dp[i][j] = dp[i+1][j+1] + 1
				t := min(dp[i][j], j-i)
				result = max(result, t)
			}
		}
	}
	fmt.Println(result)
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
