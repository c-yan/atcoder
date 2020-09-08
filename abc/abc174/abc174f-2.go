// BIT (Binary indexed tree)
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

	c := make([]int, N)
	for i := 0; i < N; i++ {
		c[i] = readInt()
	}

	lr := make([][3]int, Q)
	for i := 0; i < Q; i++ {
		l := readInt() - 1
		r := readInt() - 1
		lr[i] = [3]int{i, l, r}
	}
	sort.Slice(lr, func(i, j int) bool { return lr[i][2] < lr[j][2] })

	result := make([]int, Q)
	bit := newBIT(N)
	mr := map[int]int{}
	k := 0
	for i := 0; i < N; i++ {
		if j, ok := mr[c[i]]; ok {
			bit.add(j, -1)
		}
		bit.add(i, 1)
		mr[c[i]] = i
		for k < Q && lr[k][2] == i {
			result[lr[k][0]] = bit.query(lr[k][1], lr[k][2]+1)
			k++
		}
	}

	for i := 0; i < Q; i++ {
		println(result[i])
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
