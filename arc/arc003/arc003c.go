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
	N            int
	M            int
	c            []string
	pt           []float64
	uninvadables [][2]int
	sy           int
	sx           int
	gy           int
	gx           int
)

func isOk(m float64) bool {
	dp := make([][]bool, N)
	for y := 0; y < N; y++ {
		dp[y] = make([]bool, M)
	}
	dp[sy][sx] = true
	for i := 0; i < len(uninvadables); i++ {
		y, x := uninvadables[i][0], uninvadables[i][1]
		dp[y][x] = true
	}
	q := make([][3]int, 0)
	q = append(q, [3]int{sy, sx, 0})
	for len(q) != 0 {
		y, x, t := q[0][0], q[0][1], q[0][2]
		q = q[1:]
		for _, d := range [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
			ny, nx := y+d[0], x+d[1]
			if ny < 0 || ny >= N || nx < 0 || nx >= M {
				continue
			}
			if c[ny][nx] == 'g' {
				return true
			}
			if dp[ny][nx] {
				continue
			}
			if float64(c[ny][nx]-'0')*pt[t+1] < m {
				continue
			}
			dp[ny][nx] = true
			q = append(q, [3]int{ny, nx, t + 1})
		}
	}
	return false
}

func main() {
	defer flush()

	N = readInt()
	M = readInt()
	c = make([]string, N)
	for i := 0; i < N; i++ {
		c[i] = readString()
	}

	pt = make([]float64, 500*500)
	for i := 1; i < 500*500; i++ {
		pt[i] = math.Pow(0.99, float64(i))
	}

	uninvadables = make([][2]int, 0)
	for y := 0; y < N; y++ {
		for x := 0; x < M; x++ {
			if c[y][x] == 's' {
				sy, sx = y, x
			}
			if c[y][x] == 'g' {
				gy, gx = y, x
			}
			if c[y][x] == '#' {
				uninvadables = append(uninvadables, [2]int{y, x})
			}
		}
	}

	ok := -1e-9
	ng := 10.0
	for ng-ok > 1e-9 {
		m := (ok + ng) / 2.0
		if isOk(m) {
			ok = m
		} else {
			ng = m
		}
	}
	if ok == -1e-9 {
		println(-1)
	} else {
		println(ok)
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
