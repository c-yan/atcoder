package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	defer flush()

	N := readInt()
	S := readString()

	a := make([]int, N+1)
	g := make([]int, N+1)
	c := make([]int, N+1)
	t := make([]int, N+1)

	for i := 0; i < N; i++ {
		if S[i] == 'A' {
			a[i+1] = 1
		} else if S[i] == 'G' {
			g[i+1] = 1
		} else if S[i] == 'C' {
			c[i+1] = 1
		} else if S[i] == 'T' {
			t[i+1] = 1
		}
	}

	for i := 0; i < N; i++ {
		a[i+1] += a[i]
		g[i+1] += g[i]
		c[i+1] += c[i]
		t[i+1] += t[i]
	}

	result := 0
	for i := 0; i < N; i++ {
		for j := i + 2; j < N+1; j += 2 {
			k := a[j] - a[i]
			l := g[j] - g[i]
			m := c[j] - c[i]
			n := t[j] - t[i]
			if k == n && l == m {
				result++
			}
		}
	}
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
