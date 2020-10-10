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

func main() {
	defer flush()

	H := readInt()
	W := readInt()
	S := make([]string, H)
	for i := 0; i < H; i++ {
		S[i] = readString()
	}

	K := H * W
	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			if S[i][j] == '#' {
				K--
			}
		}
	}

	yoko := make([][]int, H)
	tate := make([][]int, H)
	for i := 0; i < H; i++ {
		yoko[i] = make([]int, W)
		tate[i] = make([]int, W)
	}

	for i := 0; i < H; i++ {
		s := 0
		l := 0
		for j := 0; j < W; j++ {
			if S[i][j] == '#' {
				for k := s; k < j; k++ {
					yoko[i][k] = l
				}
				s = j + 1
				l = 0
			} else if S[i][j] == '.' {
				l++
			}
		}
		for k := s; k < W; k++ {
			yoko[i][k] = l
		}
	}

	for i := 0; i < W; i++ {
		s := 0
		l := 0
		for j := 0; j < H; j++ {
			if S[j][i] == '#' {
				for k := s; k < j; k++ {
					tate[k][i] = l
				}
				s = j + 1
				l = 0
			} else if S[j][i] == '.' {
				l++
			}
		}
		for k := s; k < H; k++ {
			tate[k][i] = l
		}
	}

	t := make([]int, K+1)
	t[0] = 1
	for i := 1; i < K+1; i++ {
		t[i] = t[i-1] * 2
		t[i] %= m
	}

	c := 0
	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			if S[i][j] == '#' {
				continue
			}
			c += t[K-tate[i][j]-yoko[i][j]+1]
			c %= m
		}
	}

	result := K * t[K]
	result %= m
	result -= c
	result += m
	result %= m
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
