// DP(配るDP)
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func main() {
	H := readInt()
	N := readInt()

	dp := make([]int, H+1)
	fill(dp, math.MaxInt64)

	dp[0] = 0
	for i := 0; i < N; i++ {
		A := readInt()
		B := readInt()
		for j := 0; j < H; j++ {
			if dp[j] == math.MaxInt64 {
				continue
			}
			t := min(j+A, H)
			if dp[j]+B < dp[t] {
				dp[t] = dp[j] + B
			}
		}
	}

	fmt.Println(dp[H])
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

func fill(a []int, x int) {
	for i := 0; i < len(a); i++ {
		a[i] = x
	}
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
