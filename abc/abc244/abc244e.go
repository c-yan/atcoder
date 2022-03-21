package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	defer flush()

	m := 998244353

	N := readInt()
	M := readInt()
	K := readInt()
	S := readInt() - 1
	T := readInt() - 1
	X := readInt() - 1

	U := make([]int, M)
	V := make([]int, M)
	for i := 0; i < M; i++ {
		U[i] = readInt() - 1
		V[i] = readInt() - 1
	}

	dp := make([][]int, 2)
	dp[0] = make([]int, N)
	dp[1] = make([]int, N)
	dp[0][S] = 1

	for i := 0; i < K; i++ {
		t := make([][]int, 2)
		t[0] = make([]int, N)
		t[1] = make([]int, N)

		for j := 0; j < M; j++ {
			u := U[j]
			v := V[j]
			if v == X {
				if dp[0][u] != 0 {
					t[1][v] += dp[0][u]
					t[1][v] %= m
				}
				if dp[1][u] != 0 {
					t[0][v] += dp[1][u]
					t[0][v] %= m
				}
			} else {
				if dp[0][u] != 0 {
					t[0][v] += dp[0][u]
					t[0][v] %= m
				}
				if dp[1][u] != 0 {
					t[1][v] += dp[1][u]
					t[1][v] %= m
				}
			}

			if u == X {
				if dp[0][v] != 0 {
					t[1][u] += dp[0][v]
					t[1][u] %= m
				}
				if dp[1][v] != 0 {
					t[0][u] += dp[1][v]
					t[0][u] %= m
				}
			} else {
				if dp[0][v] != 0 {
					t[0][u] += dp[0][v]
					t[0][u] %= m
				}
				if dp[1][v] != 0 {
					t[1][u] += dp[1][v]
					t[1][u] %= m
				}
			}

		}

		dp = t
	}
	println(dp[0][T])
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
