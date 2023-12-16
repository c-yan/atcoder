package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// BIT stands for binary indexed tree.
type BIT []int

func newBIT(n int) BIT {
	return make([]int, n)
}

func (bit BIT) add(i, v int) {
	for i++; i <= len(bit); i += i & -i {
		bit[i-1] += v
	}
}

func (bit BIT) sum(i int) int {
	result := 0
	for i++; i > 0; i -= i & -i {
		result += bit[i-1]
	}
	return result
}

func (bit BIT) query(start int, stop int) int {
	return bit.sum(stop-1) - bit.sum(start-1)
}

func main() {
	defer flush()

	N := readInt()
	Q := readInt()

	a := make([]int, N)
	for i := 0; i < N; i++ {
		a[i] = readInt()
	}

	bit := newBIT(N)
	for i := 0; i < N; i++ {
		bit.add(i, a[i])
	}

	for i := 0; i < Q; i++ {
		t := readInt()
		if t == 0 {
			p := readInt()
			x := readInt()
			bit.add(p, x)
		} else if t == 1 {
			l := readInt()
			r := readInt()
			println(bit.query(l, r))
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
