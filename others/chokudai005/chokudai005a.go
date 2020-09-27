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

func fill(d [][]byte, i, j int, x, y byte) {
	q := [][2]int{{i, j}}
	for len(q) != 0 {
		m, n := q[0][0], q[0][1]
		q = q[1:]
		d[m][n] = x
		if m > 0 {
			if d[m-1][n] == y {
				q = append(q, [2]int{m - 1, n})
			}
		}
		if m < N-1 {
			if d[m+1][n] == y {
				q = append(q, [2]int{m + 1, n})
			}
		}
		if n > 0 {
			if d[m][n-1] == y {
				q = append(q, [2]int{m, n - 1})
			}
		}
		if n < N-1 {
			if d[m][n+1] == y {
				q = append(q, [2]int{m, n + 1})
			}
		}
	}
}

//
var (
	N int
)

func main() {
	defer flush()

	_ = readInt()
	N = readInt()
	K := readInt()

	S := make([]string, N)
	for i := 0; i < N; i++ {
		S[i] = readString()
	}

	d := make([][]byte, N)
	for i := 0; i < N; i++ {
		d[i] = make([]byte, N)
	}

	result := make([][]string, 0, K)
	for n := 1; n <= K; n++ {
		x := byte(n + '0')
		t := make([]string, 0, 10000)

		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				d[i][j] = S[i][j]
			}
		}

		for i := 1; i < N-1; i++ {
			for j := 1; j < N-1; j++ {
				if d[i][j] == x {
					continue
				}

				a := 0
				b := 0
				if d[i-1][j] != d[i][j] {
					a++
					if d[i-1][j] == d[i+1][j] {
						a++
					}
					if d[i-1][j] == d[i][j+1] && d[i-1][j] != d[i-1][j+1] {
						a++
					}
				}
				if d[i][j-1] != d[i][j] {
					b++
					if d[i][j-1] == d[i+1][j] && d[i][j-1] != d[i+1][j-1] {
						b++
					}
					if d[i][j-1] == d[i][j+1] {
						b++
					}
				}

				if a == 0 && b == 0 {
					continue
				}

				var c byte
				if a >= b {
					c = d[i-1][j]
				} else {
					c = d[i][j-1]
				}
				t = append(t, fmt.Sprintf("%d %d %c", i+1, j+1, c))
				fill(d, i, j, c, d[i][j])
			}
		}

		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if d[i][j] == x {
					continue
				}

				t = append(t, fmt.Sprintf("%d %d %c", i+1, j+1, x))
				fill(d, i, j, x, d[i][j])
			}
		}
		result = append(result, t)
	}

	best := math.MaxInt64
	for i := 0; i < K; i++ {
		best = min(best, len(result[i]))
	}

	bestIndex := -1
	for i := 0; i < K; i++ {
		if len(result[i]) == best {
			bestIndex = i
			break
		}
	}

	println(best)
	for i := 0; i < best; i++ {
		println(result[bestIndex][i])
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
