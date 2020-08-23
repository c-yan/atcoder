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

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	defer flush()

	H := readInt()
	W := readInt()
	Ch := readInt() - 1
	Cw := readInt() - 1
	Dh := readInt() - 1
	Dw := readInt() - 1
	S := make([]string, H)
	for i := 0; i < H; i++ {
		S[i] = readString()
	}

	t := make([][]int, H)
	for i := 0; i < H; i++ {
		t[i] = make([]int, W)
		for j := 0; j < W; j++ {
			if S[i][j] == '#' {
				t[i][j] = -1
			} else {
				t[i][j] = math.MaxInt64
			}
		}
	}

	warpCount := 0
	t[Ch][Cw] = warpCount
	q := make([][2]int, 0, 1024)
	q = append(q, [2]int{Ch, Cw})

	warpq := make([][2]int, 0, 1024)
	for len(q) != 0 {
		for len(q) != 0 {
			warpq = append(warpq, q[0])
			h, w := q[0][0], q[0][1]
			q = q[1:]
			if h-1 >= 0 && t[h-1][w] > warpCount {
				q = append(q, [2]int{h - 1, w})
				t[h-1][w] = t[h][w]
			}
			if h+1 < H && t[h+1][w] > warpCount {
				q = append(q, [2]int{h + 1, w})
				t[h+1][w] = t[h][w]
			}
			if w-1 >= 0 && t[h][w-1] > warpCount {
				q = append(q, [2]int{h, w - 1})
				t[h][w-1] = t[h][w]
			}
			if w+1 < W && t[h][w+1] > warpCount {
				q = append(q, [2]int{h, w + 1})
				t[h][w+1] = t[h][w]
			}
		}

		if t[Dh][Dw] != math.MaxInt64 {
			break
		}

		warpCount++
		for i := 0; i < len(warpq); i++ {
			h, w := warpq[i][0], warpq[i][1]
			for i := max(0, h-2); i <= min(H-1, h+2); i++ {
				for j := max(0, w-2); j <= min(W-1, w+2); j++ {
					if t[i][j] <= warpCount {
						continue
					}
					t[i][j] = warpCount
					q = append(q, [2]int{i, j})
				}
			}
		}
		warpq = warpq[:0]
	}

	if t[Dh][Dw] == math.MaxInt64 {
		println(-1)
	} else {
		println(t[Dh][Dw])
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
