package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func reduce(f func(x, y int) int, a []int) int {
	result := a[0]
	for i := 1; i < len(a); i++ {
		result = f(result, a[i])
	}
	return result
}

func max(x, y int) int {
	if x > y {
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
	N := readInt()
	W := readInt()

	dp := make([]int, W+1)
	fill(dp, -1)
	dp[0] = 0

	for i := 0; i < N; i++ {
		w := readInt()
		v := readInt()
		for j := W - w; j >= 0; j-- {
			if dp[j] == -1 {
				continue
			}
			dp[j+w] = max(dp[j+w], dp[j]+v)
		}
	}
	fmt.Println(reduce(max, dp))
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
