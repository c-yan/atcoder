package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

var (
	cache []int
	H, W  int
	A     [][]int
)

const (
	INF = math.MaxInt64
)

func f(y, x int) int {
	key := (y << 12) + x
	if y == H-1 && x == W-1 {
		return 0
	}
	if cache[key] != INF {
		return cache[key]
	}
	result := -INF
	if y < H-1 {
		result = max(result, A[y+1][x]-f(y+1, x))
	}
	if x < W-1 {
		result = max(result, A[y][x+1]-f(y, x+1))
	}
	cache[key] = result
	return result
}

func main() {
	defer flush()

	H = readInt()
	W = readInt()
	A = make([][]int, H)
	for i := 0; i < H; i++ {
		A[i] = make([]int, W)
		s := readString()
		for j := 0; j < W; j++ {
			if s[j] == '-' {
				A[i][j] = -1
			} else if s[j] == '+' {
				A[i][j] = 1
			}
		}
	}

	cache = make([]int, 1<<24)
	for i := 0; i < len(cache); i++ {
		cache[i] = INF
	}

	result := f(0, 0)
	if result == 0 {
		println("Draw")
	} else if result > 0 {
		println("Takahashi")
	} else if result < 0 {
		println("Aoki")
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

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
