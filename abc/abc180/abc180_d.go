package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	defer flush()

	X := readInt()
	Y := readInt()
	A := readInt()
	B := readInt()

	result := 0
	for X <= (Y-1)/A && X*A < X+B {
		X *= A
		result++
	}
	result += ((Y - 1) - X) / B
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
