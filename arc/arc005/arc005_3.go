package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func main() {
	defer flush()

	H := readInt()
	W := readInt()
	c := make([]string, H)
	for i := 0; i < H; i++ {
		c[i] = readString()
	}

	sy, sx, gy, gx := 0, 0, 0, 0
	for y := 0; y < H; y++ {
		for x := 0; x < W; x++ {
			if c[y][x] == 's' {
				sy, sx = y, x
			}
			if c[y][x] == 'g' {
				gy, gx = y, x
			}
		}
	}

	t := make([][]int, H)
	for y := 0; y < H; y++ {
		t[y] = make([]int, W)
		for x := 0; x < W; x++ {
			t[y][x] = math.MaxInt64
		}
	}
	t[sy][sx] = 0

	q := make([][2]int, 0, 4096)
	q = append(q, [2]int{sy, sx})
	for len(q) != 0 {
		y, x := q[0][0], q[0][1]
		q = q[1:]
		for _, d := range [][2]int{[2]int{-1, 0}, [2]int{1, 0}, [2]int{0, -1}, [2]int{0, 1}} {
			dy, dx := d[0], d[1]
			ny, nx := y+dy, x+dx
			if ny < 0 || ny >= H || nx < 0 || nx >= W {
				continue
			}
			switch c[ny][nx] {
			case 's', 'g', '.':
				if t[ny][nx] > t[y][x] {
					t[ny][nx] = t[y][x]
					q = append(q, [2]int{ny, nx})
				}
			case '#':
				if t[ny][nx] > t[y][x]+1 {
					t[ny][nx] = t[y][x] + 1
					q = append(q, [2]int{ny, nx})
				}
			}
		}
	}

	if t[gy][gx] <= 2 {
		println("YES")
	} else {
		println("NO")
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
