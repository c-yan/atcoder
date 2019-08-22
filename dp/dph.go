package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const divisor = 1000000007

func main() {
	h := readInt()
	w := readInt()
	a := make([]string, 2)
	a[0] = readString()
	a[1] = readString()
	dp := make([][]int, 2)
	dp[0] = make([]int, w)
	dp[1] = make([]int, w)
	dp[0][0] = 1
	for i := 0; i < h-1; i++ {
		for j := 0; j < w-1; j++ {
			if a[0][j+1] != '#' {
				dp[0][j+1] = (dp[0][j+1] + dp[0][j]) % divisor
			}
			if a[1][j] != '#' {
				dp[1][j] = dp[0][j]
			}
		}
		if a[1][w-1] != '#' {
			dp[1][w-1] = dp[0][w-1]
		}
		a[0], a[1] = a[1], readString()
		dp[0], dp[1] = dp[1], dp[0]
		for j := 0; j < w; j++ {
			dp[1][j] = 0
		}
	}
	for j := 0; j < w-1; j++ {
		if a[0][j+1] != '#' {
			dp[0][j+1] = (dp[0][j+1] + dp[0][j]) % divisor
		}
	}
	fmt.Println(dp[0][w-1])
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

func printIntln(v ...int) {
	b := make([]byte, 0, 4096)
	for i := 0; i < len(v)-1; i++ {
		b = append(b, strconv.Itoa(v[i])...)
		b = append(b, " "...)
	}
	b = append(b, strconv.Itoa(v[len(v)-1])...)
	fmt.Println(string(b))
}
