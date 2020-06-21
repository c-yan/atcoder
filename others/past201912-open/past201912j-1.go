package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

//
var (
	H int
	W int
	A [][]int
)

func fill(a []int, x int) {
	for i := 0; i < len(a); i++ {
		a[i] = x
	}
}

func costFrom(y1, x1 int) [][]int {
	dp := make([][]int, H)
	for i := 0; i < H; i++ {
		dp[i] = make([]int, W)
		fill(dp[i], math.MaxInt64)
	}

	dp[y1][x1] = 0
	q := [][2]int{{y1, x1}}
	for len(q) != 0 {
		y, x := q[0][0], q[0][1]
		q = q[1:]
		t := dp[y][x]
		if y-1 >= 0 {
			u := t + A[y-1][x]
			if dp[y-1][x] > u {
				dp[y-1][x] = u
				q = append(q, [2]int{y - 1, x})
			}
		}
		if y+1 < H {
			u := t + A[y+1][x]
			if dp[y+1][x] > u {
				dp[y+1][x] = t + A[y+1][x]
				q = append(q, [2]int{y + 1, x})
			}
		}
		if x-1 >= 0 {
			u := t + A[y][x-1]
			if dp[y][x-1] > u {
				dp[y][x-1] = u
				q = append(q, [2]int{y, x - 1})
			}
		}
		if x+1 < W {
			u := t + A[y][x+1]
			if dp[y][x+1] > u {
				dp[y][x+1] = u
				q = append(q, [2]int{y, x + 1})
			}
		}
	}
	return dp
}

func main() {
	H = readInt()
	W = readInt()
	A = make([][]int, H)
	for i := 0; i < H; i++ {
		A[i] = make([]int, W)
		for j := 0; j < W; j++ {
			A[i][j] = readInt()
		}
	}

	result := math.MaxInt64
	cost1 := costFrom(H-1, 0)
	cost2 := costFrom(H-1, W-1)
	cost3 := costFrom(0, W-1)
	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			t := cost1[i][j] + cost2[i][j] + cost3[i][j] - 2*A[i][j]
			if t < result {
				result = t
			}
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
