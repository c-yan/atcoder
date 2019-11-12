package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func pow(base int, exponent int) int {
	if exponent == 0 {
		return 1
	}

	result := 1
	for exponent > 0 {
		if exponent%2 == 1 {
			result *= base
			result %= 998244353
		}
		exponent >>= 1
		base *= base
		base %= 998244353
	}
	return result
}

func main() {
	N := readInt()
	D := readInts(N)

	if D[0] != 0 {
		fmt.Println(0)
		return
	}

	c := map[int]int{}
	maxD := 0
	for _, i := range D {
		c[i]++
		if i > maxD {
			maxD = i
		}
	}

	if c[0] != 1 {
		fmt.Println(0)
		return
	}

	result := 1
	for i := 1; i <= maxD; i++ {
		if _, ok := c[i]; !ok {
			fmt.Println(0)
			return
		}
		result *= pow(c[i-1], c[i])
		result %= 998244353
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
