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

//
var (
	A  [10000]int
	r  [10000]int
	l  [10000]int
	st [10000]int
)

func main() {
	defer flush()

	N := readInt()
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	t := 0
	for i := N - 1; i >= 0; i-- {
		for t > 0 && A[st[t-1]] >= A[i] {
			t--
		}
		if t == 0 {
			r[i] = N
		} else {
			r[i] = st[t-1]
		}
		st[t] = i
		t++
	}

	t = 0
	result := 0
	for i := 0; i < N; i++ {
		for t > 0 && A[st[t-1]] >= A[i] {
			t--
		}
		if t == 0 {
			l[i] = 0
		} else {
			l[i] = st[t-1] + 1
		}
		st[t] = i
		t++
		result = max(result, A[i]*(r[i]-l[i]))
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
