package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func main() {
	AMax := 10000

	H := readInt()
	N := readInt()
	AB := make([]struct{ A, B int }, N)
	for i := 0; i < N; i++ {
		AB[i].A = readInt()
		AB[i].B = readInt()
	}

	dpLen := H + AMax + 1
	dp := make([]int, dpLen)
	for i := 0; i < dpLen; i++ {
		dp[i] = math.MaxInt64
	}

	dp[0] = 0
	for i := 0; i < H; i++ {
		if dp[i] == math.MaxInt64 {
			continue
		}
		for j := 0; j < N; j++ {
			a := AB[j].A
			b := AB[j].B
			if dp[i]+b < dp[i+a] {
				dp[i+a] = dp[i] + b
			}
		}
	}

	result := math.MaxInt64
	for i := H; i < dpLen; i++ {
		if dp[i] < result {
			result = dp[i]
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
