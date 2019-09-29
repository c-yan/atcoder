package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func fill(s []int, x int) {
	for i := 0; i < len(s); i++ {
		s[i] = x
	}
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func readKey() [2]int {
	a := readInt()
	b := readInt()
	m := 0
	for i := 0; i < b; i++ {
		c := readInt()
		m |= 1 << uint(c-1)
	}
	return [2]int{a, m}
}

func main() {
	N := readInt()
	M := readInt()
	keys := make([][2]int, M)
	for i := 0; i < M; i++ {
		keys[i] = readKey()
	}

	dp := make([]int, 1<<uint(N))
	fill(dp, math.MaxInt64)

	dp[0] = 0
	for i := 0; i < M; i++ {
		a, m := keys[i][0], keys[i][1]
		for j := (1 << uint(N)) - 1; j >= 0; j-- {
			if dp[j] == math.MaxInt64 {
				continue
			}
			dp[j|m] = min(dp[j|m], dp[j]+a)
		}
	}
	if dp[(1<<uint(N))-1] == math.MaxInt64 {
		fmt.Println(-1)
	} else {
		fmt.Println(dp[(1<<uint(N))-1])
	}
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
