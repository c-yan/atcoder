// 累積和
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	H := readInt()
	W := readInt()
	S := make([]string, H)
	for i := 0; i < H; i++ {
		S[i] = readString()
	}

	L := make([][]int, H)
	R := make([][]int, H)
	U := make([][]int, H)
	D := make([][]int, H)
	for i := 0; i < H; i++ {
		L[i] = make([]int, W)
		R[i] = make([]int, W)
		U[i] = make([]int, W)
		D[i] = make([]int, W)
	}

	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			if j == 0 {
				if S[i][0] == '.' {
					L[i][0] = 1
				}
				if S[i][W-1] == '.' {
					R[i][W-1] = 1
				}
			} else {
				if S[i][j] == '.' {
					L[i][j] = L[i][j-1] + 1
				}
				if S[i][W-1-j] == '.' {
					R[i][W-1-j] = R[i][W-1-j+1] + 1
				}
			}
			if i == 0 {
				if S[0][j] == '.' {
					U[0][j] = 1
				}
				if S[H-1][j] == '.' {
					D[H-1][j] = 1
				}
			} else {
				if S[i][j] == '.' {
					U[i][j] = U[i-1][j] + 1
				}
				if S[H-1-i][j] == '.' {
					D[H-1-i][j] = D[H-1-i+1][j] + 1
				}
			}
		}
	}

	result := 0
	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			t := L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3
			result = max(result, t)
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
