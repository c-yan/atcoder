// DP
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

func fill(a []int, x int) {
	for i := 0; i < len(a); i++ {
		a[i] = x
	}
}

func main() {
	const maxW = 100000

	N := readInt()
	W := readInt()

	dp := make([]int, maxW+1)
	fill(dp, math.MaxInt64)
	dp[0] = 0

	for i := 0; i < N; i++ {
		w := readInt()
		v := readInt()
		for j := maxW - v; j >= 0; j-- {
			if dp[j] == math.MaxInt64 {
				continue
			}
			if dp[j]+w <= W {
				dp[j+v] = min(dp[j+v], dp[j]+w)
			}
		}
	}
	i := maxW
	for dp[i] == math.MaxInt64 {
		i--
	}
	fmt.Println(i)
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
