package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	a      []int
	dp     [][][2]int
	calced [][]bool
)

func f(u, l, r int) [2]int {
	if l > r {
		return [2]int{0, 0}
	}
	if calced[l][r] {
		return dp[l][r]
	}
	calced[l][r] = true
	t0 := f(u^1, l+1, r)
	t0[u] += a[l]
	t1 := f(u^1, l, r-1)
	t1[u] += a[r]
	if t0[u]-t0[u^1] > t1[u]-t1[u^1] {
		dp[l][r] = t0
	} else {
		dp[l][r] = t1
	}
	return dp[l][r]
}

func main() {
	N := readInt()
	a = make([]int, N)
	for i := 0; i < N; i++ {
		a[i] = readInt()
	}

	dp = make([][][2]int, N)
	calced = make([][]bool, N)
	for i := 0; i < N; i++ {
		dp[i] = make([][2]int, N)
		calced[i] = make([]bool, N)
	}

	t := f(0, 0, N-1)
	fmt.Println(t[0] - t[1])
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
