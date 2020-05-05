// ワーシャルフロイド
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func warshallFloyd(n int, d [][]int) {
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				d[i][j] = min(d[i][j], d[i][k]+d[k][j])
			}
		}
	}
}

func main() {
	H := readInt()
	W := readInt()

	S := make([]string, H)
	for i := 0; i < H; i++ {
		S[i] = readString()
	}

	n := H * W
	d := make([][]int, n)
	for i := 0; i < n; i++ {
		d[i] = make([]int, n)
		fillInts(d[i], math.MaxInt32)
		d[i][i] = 0
	}

	for y := 0; y < H; y++ {
		for x := 0; x < W; x++ {
			if S[y][x] == '#' {
				continue
			}
			if y-1 >= 0 && S[y-1][x] != '#' {
				d[y*W+x][(y-1)*W+x] = 1
			}
			if y+1 < H && S[y+1][x] != '#' {
				d[y*W+x][(y+1)*W+x] = 1
			}
			if x-1 >= 0 && S[y][x-1] != '#' {
				d[y*W+x][y*W+x-1] = 1
			}
			if x+1 < W && S[y][x+1] != '#' {
				d[y*W+x][y*W+x+1] = 1
			}
		}
	}

	warshallFloyd(n, d)

	result := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if d[i][j] < math.MaxInt32 && d[i][j] > result {
				result = d[i][j]
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

func fillInts(a []int, x int) {
	for i := 0; i < len(a); i++ {
		a[i] = x
	}
}
