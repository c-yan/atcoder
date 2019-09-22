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

type intSlice []int

func (s intSlice) max() int {
	result := s[0]
	for i := 1; i < len(s); i++ {
		result = max(result, s[i])
	}
	return result
}

func (s intSlice) fill(x int) {
	for i := 0; i < len(s); i++ {
		s[i] = x
	}
}

func main() {
	N := readInt()
	W := readInt()

	dp := make(intSlice, W+1)
	dp.fill(-1)
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
	fmt.Println(dp.max())
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
