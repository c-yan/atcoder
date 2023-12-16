package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	m = 1000000007
)

//
var (
	H  int
	W  int
	a  [][]int
	dp [][]int
)

func f(y int, x int) int {
	if dp[y][x] != 0 {
		return dp[y][x]
	}

	result := 1
	for _, d := range [][2]int{[2]int{-1, 0}, [2]int{1, 0}, [2]int{0, -1}, [2]int{0, 1}} {
		ny := y + d[0]
		nx := x + d[1]
		if ny < 0 || ny >= H || nx < 0 || nx >= W {
			continue
		}
		if a[ny][nx] <= a[y][x] {
			continue
		}
		result += f(ny, nx)
		result %= m
	}
	dp[y][x] = result
	return result
}

func main() {
	defer flush()

	H = readInt()
	W = readInt()

	a = make([][]int, H)
	dp = make([][]int, H)
	for y := 0; y < H; y++ {
		a[y] = make([]int, W)
		dp[y] = make([]int, W)
		for x := 0; x < W; x++ {
			a[y][x] = readInt()
		}
	}

	result := 0
	for y := 0; y < H; y++ {
		for x := 0; x < W; x++ {
			result += f(y, x)
			result %= m
		}
	}
	println(result)
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

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
