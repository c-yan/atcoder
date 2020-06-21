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
	Q := readInt()

	transposed := false
	rows := make([]int, N+1)
	cols := make([]int, N+1)
	for i := 0; i < N+1; i++ {
		rows[i] = i
		cols[i] = i
	}

	for k := 0; k < Q; k++ {
		Q := readInt()
		if Q == 1 {
			A := readInt()
			B := readInt()
			if !transposed {
				t := rows[A]
				rows[A] = rows[B]
				rows[B] = t
			} else {
				t := cols[A]
				cols[A] = cols[B]
				cols[B] = t
			}
		} else if Q == 2 {
			A := readInt()
			B := readInt()
			if !transposed {
				t := cols[A]
				cols[A] = cols[B]
				cols[B] = t
			} else {
				t := rows[A]
				rows[A] = rows[B]
				rows[B] = t
			}
		} else if Q == 3 {
			transposed = !transposed
		} else if Q == 4 {
			A := readInt()
			B := readInt()
			i, j := A, B
			if transposed {
				i, j = j, i
			}
			i = rows[i]
			j = cols[j]
			println(N*(i-1) + j - 1)
		}
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
