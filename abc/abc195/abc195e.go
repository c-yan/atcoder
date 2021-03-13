package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	N  int
	S  string
	X  string
	dp []map[int]bool
)

func f(i int, r int) bool {
	if i == N {
		return r%7 == 0
	}

	if val, ok := dp[i][r]; ok {
		return val
	}

	if X[i] == 'A' {
		b := f(i+1, (r*10)%7)
		if !b {
			dp[i][r] = b
			return b
		}
		b = f(i+1, (r*10+(int)(S[i]-'0'))%7)
		dp[i][r] = b
		return b
	} else if X[i] == 'T' {
		b := f(i+1, (r*10)%7)
		if b {
			dp[i][r] = b
			return b
		}
		b = f(i+1, (r*10+(int)(S[i]-'0'))%7)
		dp[i][r] = b
		return b
	} else {
		panic("invalid input")
	}
}

func main() {
	defer flush()

	N = readInt()
	S = readString()
	X = readString()

	dp = make([]map[int]bool, N)
	for i := 0; i < N; i++ {
		dp[i] = make(map[int]bool)
	}

	if f(0, 0) {
		println("Takahashi")
	} else {
		println("Aoki")
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
