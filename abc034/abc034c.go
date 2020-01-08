package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	M = 1000000007
)

var (
	fac  []int
	ifac []int
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func mpow(x int, n int) int {
	ans := 1
	for n != 0 {
		if n&1 == 1 {
			ans = ans * x % M
		}
		x = x * x % M
		n = n >> 1
	}
	return ans
}

func comb(a int, b int) int {
	if a == 0 && b == 0 {
		return 1
	}
	if a < b || a < 0 {
		return 0
	}
	tmp := ifac[a-b] * ifac[b] % M
	return tmp * fac[a] % M
}

func main() {
	W := readInt()
	H := readInt()

	fac = make([]int, 200001)
	ifac = make([]int, 200001)

	fac[0] = 1
	ifac[0] = 1
	for i := 0; i < 200000; i++ {
		fac[i+1] = fac[i] * (i + 1) % M
		ifac[i+1] = ifac[i] * mpow(i+1, M-2) % M
	}

	fmt.Println(comb(W + H - 2, min(W - 1, H - 1)) % M)
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
