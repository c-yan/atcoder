package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	n := readInt()
	q := readInt()

	results := make([]int, n+1)
	parents := make([]int, n+1)

	for i := 0; i < n-1; i++ {
		a := readInt()
		b := readInt()
		parents[b] = a
	}

	for i := 0; i < q; i++ {
		p := readInt()
		x := readInt()
		results[p] += x
	}

	for i := 1; i <= n; i++ {
		results[i] += results[parents[i]]
	}

	for i := 1; i <= n; i++ {
		writeInt(results[i])
		if i != n {
			writeString(" ")
		}
	}
	writeNewLineAndFlush()
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

var stdoutWriter = bufio.NewWriter(os.Stdout)

func readString() string {
	stdinScanner.Scan()
	return stdinScanner.Text()
}

func readInt() int {
	result, _ := strconv.Atoi(readString())
	return result
}

func writeString(s string) {
	stdoutWriter.WriteString(s)
}

func writeInt(i int) {
	writeString(strconv.Itoa(i))
}

func writeNewLineAndFlush() {
	stdoutWriter.WriteString("\n")
	stdoutWriter.Flush()
}
