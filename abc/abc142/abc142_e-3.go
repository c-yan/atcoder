package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var (
	N  int
	M  int
	dp []int
)

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
		m |= 1 << uint(readInt()-1)
	}
	return [2]int{a, m}
}

func readKeys() (result [][2]int) {
	for i := 0; i < M; i++ {
		result = append(result, readKey())
	}
	return
}

func solve(keys [][2]int, amount int, cm int) int {
	if cm == (1<<uint(N))-1 {
		return amount
	}
	if len(keys) == 0 {
		return math.MaxInt64
	}
	a := keys[0][0]
	m := keys[0][1]
	if dp[cm|m] < amount+a {
		return solve(keys[1:], amount, cm)
	}
	dp[cm|m] = amount + a
	return min(solve(keys[1:], amount+a, cm|m), solve(keys[1:], amount, cm))
}

func main() {
	N = readInt()
	M = readInt()
	keys := readKeys()

	dp = make([]int, 1<<uint(N))
	for i := 0; i < 1<<uint(N); i++ {
		dp[i] = math.MaxInt64
	}

	t := solve(keys, 0, 0)
	if t == math.MaxInt64 {
		fmt.Println(-1)
	} else {
		fmt.Println(t)
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
