package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func main() {
	N := readInt()

	if N == 2 {
		// K = 2
		fmt.Println(1)
		return
	}

	result := 2 // K = N - 1, N
	for K := 2; K <= int(math.Sqrt(float64(N))); K++ {
		t := N
		for t >= K && t%K == 0 {
			t /= K
		}
		if t%K == 1 {
			result++
		}

		if (N-1)%K == 0 && (N-1)/K > K {
			result++
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

func readInts(n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = readInt()
	}
	return result
}
